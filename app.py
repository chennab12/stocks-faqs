import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from content import LESSONS,SOURCES,MISTAKES,ISSUES
from calculations import growth,required_monthly,recovery,weighted_return
st.set_page_config(page_title='Stocks & Investing Compass',page_icon='📈',layout='wide')
st.title('📈 Stocks & Investing Compass')
st.caption('Basics → intermediate → advanced · US investor education · Reviewed October 1, 2026')
st.info('Learn concepts and test assumptions. Examples are hypothetical, returns are uncertain, and tax rules depend on your circumstances. No live prices or buy/sell signals are used.')
q=st.sidebar.text_input('Search cheatsheet',placeholder='ETF, fees, RSU…')
st.sidebar.caption('All tabs remain available. Search filters only the master table.')

def memory(title,meaning):
    # Code-native animated illustration; all educational motion respects reduced-motion preference.
    import html
    components.html(f'''<style>body{{font-family:system-ui;color:#17324d}}.card{{background:#eef5ff;border-radius:14px;padding:18px}}.tokens{{display:flex;gap:18px;font-size:30px}}.coin{{animation:bob 2s ease-in-out infinite}}.coin:nth-child(2){{animation-delay:.3s}}@keyframes bob{{50%{{transform:translateY(-8px)}}}}@media(prefers-reduced-motion:reduce){{.coin{{animation:none}}}}</style><div class="card"><b>{html.escape(title)}</b><div class="tokens"><span class="coin">📚</span><span>→</span><span class="coin">🧮</span><span>→</span><span class="coin">🧭</span></div><p>{html.escape(meaning)}</p><small>Read the evidence → check the math → apply your plan.</small></div>''',height=180)

def table(rows):st.dataframe(pd.DataFrame(rows),hide_index=True,use_container_width=True)
rows=[]
for title,level,source,concepts,question,answer in LESSONS:
    for concept,meaning,example,action,metric in concepts:
        rows.append({'Area':title,'Level':level,'Concept':concept,'Meaning':meaning,'Intuitive example':example,'Do':action,'Don’t':'Treat this metric as a stand-alone decision rule.','Myth vs fact':'A single number cannot establish suitability or guarantee returns.','Key metric / formula':metric,'Suggested next step':'Apply this concept to one hypothetical holding and record assumptions.','Source':SOURCES[source]})
tabs=st.tabs(['📌 Master cheatsheet','🏠 Start here']+[x[0] for x in LESSONS]+['🧮 Calculators','⚖️ Compare approaches','📝 Research & goals','📚 Sources'])
with tabs[0]:
    st.subheader('Investing essentials at a glance')
    df=pd.DataFrame(rows)
    if q:df=df[df.astype(str).apply(lambda c:c.str.contains(q,case=False,regex=False)).any(axis=1)]
    st.dataframe(df,hide_index=True,use_container_width=True,column_config={'Source':st.column_config.LinkColumn('Source')})
    st.download_button('Download master CSV',df.to_csv(index=False).encode(),file_name='stocks_investing_cheatsheet.csv')
    st.subheader('Common mistakes and how to avoid them')
    table([dict(zip(['Mistake','Why it happens','How to avoid it','Tools / help'],r)) for r in MISTAKES])
    st.subheader('Common investing issues')
    table([dict(zip(['Issue','Root cause','Practical response','Tools / help'],r)) for r in ISSUES])
    st.subheader('Formula reference')
    table([{'Calculation':'Total return','Formula':'(ending value − initial value + distributions) / initial value','Limitation':'No external contributions; costs and taxes must be consistently included'}, {'Calculation':'Inflation-adjusted return','Formula':'(1 + nominal return) / (1 + inflation) − 1','Limitation':'Use the same period'}, {'Calculation':'Recovery after loss','Formula':'loss / (1 − loss)','Limitation':'A 50% loss needs a 100% gain'}, {'Calculation':'Portfolio company exposure','Formula':'direct weight + Σ(fund weight × company weight in fund)','Limitation':'Requires up-to-date holdings'}])
with tabs[1]:
    st.subheader('A repeatable investing decision')
    st.write('Define the goal and horizon, assess risk capacity, choose suitable exposure, inspect costs and taxes, then follow a review plan.')
    a,b,c=st.columns(3);a.metric('Lessons',len(LESSONS));b.metric('Core concepts',len(rows));c.metric('Calculator modes',7)
    table([{'Sequence':i+1,'Topic':x[0],'Level':x[1]} for i,x in enumerate(LESSONS)])
    memory('Plan before purchasing','Start with when you need the money and what loss you can absorb.')
for tab,lesson in zip(tabs[2:2+len(LESSONS)],LESSONS):
    title,level,source,concepts,question,answer=lesson
    with tab:
        st.header(title);st.caption(level)
        table([dict(zip(['Concept','Plain meaning','Intuitive example','Investor takeaway','Metric / formula'],r)) for r in concepts])
        with st.expander('Knowledge check: '+question):
            st.text_area('Explain first',key='answer_'+title)
            if st.checkbox('Show expected answer',key='reveal_'+title):st.success(answer)
        st.markdown(f'[Read original guidance ↗]({SOURCES[source]})')
        st.subheader('Common mistake to avoid')
        st.write('Using a single metric or example as a decision rule. Check the time horizon, source, assumptions and downside before applying it.')
        st.subheader('Visual memory cue');memory(title,concepts[0][1]+' '+concepts[0][3])
with tabs[-4]:
    st.header('🧮 Investing calculators')
    tool=st.selectbox('Calculator',['Compound growth & fee drag','Monthly savings for a goal','Valuation ratios','Drawdown & recovery','Rebalance planner','Portfolio stress test','ESPP discount arithmetic'])
    if tool in ('Compound growth & fee drag','Monthly savings for a goal'):
        initial=st.number_input('Initial balance ($)',min_value=0.,value=10000.)
        years=st.number_input('Years',min_value=1,max_value=60,value=10)
        rate=st.slider('Assumed annual nominal return (%)',-50.,20.,5.,.5)/100
        if tool=='Monthly savings for a goal':
            target=st.number_input('Target balance ($)',min_value=0.,value=100000.)
            st.metric('Illustrative monthly contribution',f'${required_monthly(initial,target,rate,years):,.2f}')
        else:
            monthly=st.number_input('Month-end contribution ($)',min_value=0.,value=200.)
            fee=st.slider('Annual fee (%)',0.,3.,.25,.05)/100
            inflation=st.slider('Assumed annual inflation (%)',0.,10.,3.,.5)/100
            no_fee=growth(initial,monthly,rate,years);net=growth(initial,monthly,rate,years,fee)
            st.line_chart(pd.DataFrame({'No fee':no_fee,'With fee':net}).rename_axis('Month'))
            a,b,c=st.columns(3);a.metric('Ending balance',f'${net[-1]:,.0f}');b.metric('Fee impact',f'${no_fee[-1]-net[-1]:,.0f}');c.metric('In today’s dollars',f'${net[-1]/(1+inflation)**years:,.0f}')
        st.caption('Constant hypothetical returns; actual volatility, taxes and changing contributions are excluded. Annual rates are converted to effective monthly rates.')
    elif tool=='Valuation ratios':
        price=st.number_input('Share price ($)',min_value=.01,value=100.)
        eps=st.number_input('Diluted annual EPS ($)',value=5.)
        dividend=st.number_input('Annual dividend per share ($)',min_value=0.,value=2.)
        st.metric('P/E',f'{price/eps:.2f}×' if eps>0 else 'Not meaningful for EPS ≤ 0');st.metric('Dividend yield',f'{dividend/price:.2%}')
        st.caption('Trailing vs forward EPS and nonrecurring items change interpretation. No valuation verdict is produced.')
    elif tool=='Drawdown & recovery':
        loss=st.slider('Loss from peak (%)',0,99,30)/100
        st.metric('Gain needed to recover',f'{recovery(loss):.2%}')
        st.bar_chart(pd.DataFrame({'Value':[100,100*(1-loss),100]},index=['Peak','After loss','Recovered']))
    elif tool=='Rebalance planner':
        holdings=st.data_editor(pd.DataFrame({'Asset':['Stocks','Bonds','Cash'],'Current value':[6000.,3000.,1000.],'Target %':[60.,30.,10.]}),hide_index=True,num_rows='dynamic')
        if holdings['Current value'].isna().any() or holdings['Target %'].isna().any() or (holdings['Current value']<0).any() or (holdings['Target %']<0).any() or abs(holdings['Target %'].sum()-100)>.01:st.warning('Enter nonnegative values and target weights totaling 100%.')
        else:
            holdings['Target value']=holdings['Current value'].sum()*holdings['Target %']/100
            holdings['Illustrative adjustment']=holdings['Target value']-holdings['Current value'];table(holdings)
            st.caption('Positive = add; negative = reduce. Excludes tax lots, transaction costs and suitability; new contributions can reduce selling.')
    elif tool=='Portfolio stress test':
        w=st.slider('Stock weight (%)',0,100,70)/100
        stocks=st.slider('Hypothetical stock return (%)',-80,80,-30)/100
        other=st.slider('Hypothetical other-asset return (%)',-80,80,-5)/100
        st.metric('Hypothetical portfolio change',f'{weighted_return([w,1-w],[stocks,other]):.2%}')
        st.caption('Two-asset arithmetic under specified scenarios; not a probability estimate or forecast.')
    else:
        ref=st.number_input('Reference price ($)',min_value=.01,value=100.)
        discount=st.slider('Discount (%)',0.,50.,15.)/100
        paid=ref*(1-discount)
        st.metric('Illustrative purchase price',f'${paid:.2f}');st.metric('Discount / purchase price',f'{(ref-paid)/paid:.2%}')
        st.caption('A 15% discount is about 17.65% of purchase cost at an unchanged reference price. This is not an annualized return. Excludes lookback mechanics, price changes, plan restrictions and taxes.')
with tabs[-3]:
    st.header('Compare investing approaches')
    table([dict(zip(['Approach','Potential value','Tradeoff / risk','When to consider','Key check'],r)) for r in [
    ('Broad index investing','Diversified market exposure','Market losses; index concentration','When suitable for long-term goals','Holdings, fees, allocation'),
    ('Individual stock selection','Targeted business exposure','Company risk; research demands','When you can assess and manage concentration','Thesis, valuation, downside'),
    ('Active funds','Professional selection','Fees and underperformance risk','When strategy and manager fit your goal','Net results, benchmark, process'),
    ('Target-date funds','Integrated allocation path','Glide path may not match your needs','For a goal-date framework after reviewing holdings','Fees and equity exposure'),
    ('Dividend strategies','Cash distributions','Cuts, concentration and taxes','When distribution characteristics suit your plan','Total return and coverage'),
    ('Trading / options / leverage','Tactical exposures','Complex losses, costs and timing risk','Only after understanding mechanics and constraints','Maximum loss and liquidity')]])
    st.caption('The comparison describes tradeoffs; it does not select an approach for you.')
with tabs[-2]:
    st.header('Research worksheet & practical goals')
    template=pd.DataFrame({'Field':['Goal and horizon','Business / fund objective','Primary source and date','Revenue, cash and debt','Valuation assumptions','Downside scenario','Portfolio concentration','Fees and tax considerations','What would change my mind','Review date'],'My notes':['']*10})
    edited=st.data_editor(template,hide_index=True,use_container_width=True)
    st.download_button('Download research notes',edited.to_csv(index=False).encode(),file_name='investing_research.csv')
    table([{'Suggested SMART goal':'Within 7 days, write a one-page investment policy','Next step':'List horizon, liquidity needs and review rules'}, {'Suggested SMART goal':'Within 14 days, compare 3 funds using holdings, fees and objectives','Next step':'Read prospectuses and record differences'}, {'Suggested SMART goal':'Within 30 days, analyze one company’s 10-K','Next step':'Record business risks, cash-flow trends and valuation assumptions'}, {'Suggested SMART goal':'Review employer-stock concentration quarterly','Next step':'Add direct holdings and fund overlap; check plan and tax rules'}])
    st.caption('Notes remain in the current session unless downloaded; this app does not connect to a brokerage or place trades.')
with tabs[-1]:
    st.header('Official sources & method')
    st.dataframe(pd.DataFrame([{'Source':n,'Link':u} for n,u in SOURCES.items()]),hide_index=True,use_container_width=True,column_config={'Link':st.column_config.LinkColumn('Link')})
    st.write('Editorial priorities cover common beginner decisions. “High ROI” describes practical learning value, not a measured percentile or an investment-return promise. No live feeds, market history, product rankings or forecasts are fabricated. Follow linked guidance for current rules and disclosures.')
