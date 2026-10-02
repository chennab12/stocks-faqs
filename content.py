SOURCES={
'Investor.gov basics':'https://www.investor.gov/introduction-investing',
'Allocation':'https://www.investor.gov/introduction-investing/getting-started/asset-allocation',
'Fees':'https://www.investor.gov/introduction-investing/getting-started/understanding-fees',
'Stocks':'https://www.finra.org/investors/investing/investment-products/stocks',
'Orders':'https://www.finra.org/investors/investing/investment-products/stocks/order-types',
'Risk':'https://www.finra.org/investors/investing/investing-basics/risk',
'Funds':'https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-funds-etfs/mutual-funds',
'Filings':'https://www.sec.gov/search-filings',
'10-K guide':'https://www.sec.gov/files/reada10k.pdf',
'Employee equity':'https://www.irs.gov/taxtopics/tc427',
'ESPP':'https://www.irs.gov/faqs/capital-gains-losses-and-sale-of-home/stocks-options-splits-traders/stocks-options-splits-traders-5',
'Tax reference':'https://www.irs.gov/publications/p550',
'Leverage':'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/leveraged-investing-strategies-know-risks-using-these-advanced-investment-tools',
'BrokerCheck':'https://brokercheck.finra.org/'
}
# title, level, anchor source, concepts (concept, meaning, example, takeaway, metric), quiz and answer
LESSONS=[
('🌱 Goals & readiness','Basics','Investor.gov basics',[
('Time horizon','When money will be needed determines suitable risk.','A house payment in 6 months differs from retirement in 20 years.','Separate near-term spending from long-term investments.','Years until goal'),
('Risk capacity vs tolerance','Capacity is ability to absorb loss; tolerance is willingness.','A job loss plus a market decline strains cash flow.','Assess both before choosing allocation.','Monthly essential spending; liquidity runway'),
('Investment policy','Written objectives and rules reduce reactive decisions.','Set contribution, allocation and review rules.','Write a one-page plan before selecting stocks.','Review date; contribution rate')],
'Why can a good stock be unsuitable for a near-term goal?','Its price may fall when you need the money; suitability depends on your goal and ability to wait.'),
('📈 Stock fundamentals','Basics','Stocks',[
('Ownership','A share is a claim on a business, not a promised repayment.','A company can grow while its stock disappoints.','Separate business quality from purchase price.','Market cap = price × shares outstanding'),
('Total return','Return combines price change and distributions.','$100 becomes $105 and pays $2: 7% simple total return.','Include dividends, fees and taxes consistently.','R = (end − start + distributions) / start'),
('Share price vs value','Nominal share price alone says little about valuation.','A split changes price and share count without creating wealth.','Compare market capitalization and earnings.','P/E = price / EPS; meaningless if EPS ≤ 0')],
'Is a $5 stock cheaper than a $100 stock?','Not necessarily. Share counts, earnings, debt and future cash flows matter.'),
('🧺 ETFs & index funds','Basics','Funds',[
('ETF wrapper','An ETF trades on an exchange and holds underlying assets.','A narrow semiconductor ETF can remain concentrated.','Check holdings, objective and prospectus.','Expense ratio; holdings; spread'),
('Index vs active','Index funds follow a benchmark; active managers select investments.','A broad index and sector index cover different risks.','Match exposure to your plan.','Tracking difference; benchmark'),
('Fund overlap','Different fund names can hide repeated holdings.','Two tech-heavy funds may share top positions.','Inspect underlying exposure.','Look-through company weight')],
'Does holding five ETFs guarantee diversification?','No. Check asset classes, geography, sectors and overlapping holdings.'),
('🧭 Risk & diversification','Basics','Allocation',[
('Company risk','One business can fail independently of the market.','An earnings miss sharply affects one issuer.','Avoid dependence on one company.','Single-company weight = value / portfolio'),
('Market risk','Diversification cannot remove a broad market decline.','Stocks across sectors fall during a recession.','Keep a horizon and allocation you can sustain.','Drawdown = value / prior peak − 1'),
('Correlation','Assets moving together provide less diversification.','Two sector funds respond to the same demand cycle.','Evaluate underlying economic drivers.','Correlation ranges −1 to +1')],
'Can diversification eliminate losses?','No. It can reduce concentration risk, but market and other risks remain.'),
('🛒 Brokers & order types','Basics','Orders',[
('Market order','Prioritizes execution rather than an exact price.','A fast market fills above the last quote.','Understand execution and spread.','Bid–ask spread = ask − bid'),
('Limit order','Trades only at the limit price or better, if executed.','A buy limit below market may never fill.','Choose between price control and execution certainty.','Limit price; time in force'),
('Stop order','Usually becomes a market order once triggered.','A gap can produce a fill below a sell stop.','A stop price is not a guaranteed execution price.','Trigger vs fill price')],
'What is the main tradeoff of a limit order?','Price control with a risk of no execution.'),
('⏳ Compounding & contributions','Basics','Investor.gov basics',[
('Compounding','Returns earn further returns over time.','$1,000 at an assumed 5% for 10 years becomes about $1,629.','Treat the return as a scenario, not a promise.','FV = PV(1+r)^n'),
('Regular contributions','New savings can be a major source of growth.','$200 deposited at each month-end for years.','Choose a sustainable amount.','Annual savings = monthly contribution × 12'),
('Real return','Inflation reduces purchasing power.','7% nominal and 3% inflation imply about 3.88% real.','Plan in nominal or real dollars consistently.','Real r = (1+r)/(1+inflation) − 1')],
'Why should a calculator include inflation?','A larger future balance may buy less; purchasing power matters.'),
('🧾 Financial statements','Intermediate','10-K guide',[
('Income statement','Revenue, expenses and profit across a period.','Sales rise but profit falls as costs increase.','Examine margins and diluted EPS.','Net margin = net income / revenue'),
('Balance sheet','Assets, liabilities and equity at a date.','Debt can constrain a profitable business.','Assess debt maturity and liquidity.','Assets = liabilities + equity'),
('Cash-flow statement','Shows operating, investing and financing cash movements.','Reported profit can exceed operating cash flow.','Read all three statements together.','Simple FCF = operating cash flow − capital expenditures')],
'Why can profit differ from cash flow?','Accrual accounting, working capital and noncash items affect profit and cash differently.'),
('🔎 Valuation & stock research','Intermediate','Filings',[
('P/E context','Earnings multiple depends on growth, risk and earnings quality.','A low multiple can reflect a declining business.','Compare like businesses and normalized earnings.','P/E = equity value / net earnings'),
('Discounted cash flows','Future cash flows are discounted into present value.','Higher discount rates reduce estimated value.','Test assumptions and downside cases.','PV = Σ cash flow_t / (1+r)^t'),
('Investment thesis','Evidence-backed reason to own, with disconfirming signals.','Growth thesis weakens if customer retention falls.','Write what would change your mind.','Revenue growth; margin; cash conversion')],
'Why is a low P/E not an automatic bargain?','Earnings may be unsustainable or business risk may justify a lower multiple.'),
('💵 Dividends & income','Intermediate','Stocks',[
('Dividend yield','Annual dividends relative to share price.','$3 dividend on $100 price gives 3%.','Yield is not total return or guaranteed income.','Yield = annual dividend / price'),
('Dividend sustainability','Payments require financing and cash capacity.','A falling price raises yield before a dividend cut.','Inspect coverage and debt.','Payout ratio = dividends / net income'),
('Reinvestment','Purchases more shares with distributions.','Reinvested dividends compound but may be taxable.','Account for cash needs and tax treatment.','Total return includes reinvested distributions')],
'Is the highest dividend yield always best?','No. It may reflect distress, an unsustainable payout or capital losses.'),
('⚖️ Allocation & rebalancing','Intermediate','Allocation',[
('Target weights','Allocation reflects horizon, goals and risk.','An illustrative 60/40 mix is not a universal recommendation.','Set your own rationale and review rules.','Weights sum to 100%'),
('Drift','Market movements change portfolio weights.','A stock sleeve grows from 50% to 65%.','Review deviations without chasing winners.','Drift = current weight − target weight'),
('Rebalancing costs','Restoring weights may trigger costs or taxes.','Direct new contributions to underweight assets.','Consider cash flows before selling.','Target dollars = total portfolio × target weight')],
'Why rebalance after an asset rises?','To restore intended risk exposure, not because future price direction is known.'),
('💼 RSUs, ESPP & employer stock','Intermediate','ESPP',[
('Combined exposure','Salary and employer shares depend on the same company.','Job loss and share losses can coincide.','Measure company concentration across vested accounts.','Employer stock / investable portfolio'),
('ESPP','Plan rules and tax treatment affect net benefit.','A discount can coexist with price and holding-period risk.','Read plan documents and keep basis records.','Discount %; grant, purchase and sale dates'),
('RSUs and options','Different awards have different tax and exercise mechanics.','An RSU vest differs from exercising a stock option.','Check award type, blackout rules and tax records.','Vested value; withholding; cost basis')],
'Why distinguish ESPP discounts from investment returns?','A discount, stock price change and taxes are separate contributors to net proceeds.'),
('🏛️ Taxes & account types','Intermediate','Tax reference',[
('Cost basis','Tax gain depends on basis, adjustments and proceeds.','$120 sale less $100 adjusted basis gives $20 gain before costs.','Reconcile broker reports and equity compensation records.','Gain = net proceeds − adjusted basis'),
('Account wrapper','Taxable and retirement accounts have different rules.','The same fund can have different tax consequences by account.','Check eligibility, withdrawals and current limits.','After-tax outcome; withdrawal conditions'),
('Tax-loss harvesting','Loss use depends on tax rules and replacement purchases.','A wash-sale rule can defer a deduction.','Review all relevant accounts and transaction dates.','Avoid assuming every realized loss is immediately deductible')],
'Is a 1099-B always the complete answer for employee shares?','No. Compensation-related basis adjustments can matter; reconcile documents and obtain tax guidance.'),
('🧮 Performance & benchmarks','Advanced','Risk',[
('CAGR','Annualized growth for beginning and ending values without external cash flows.','$100 becomes $121 in 2 years: 10% CAGR.','Do not apply naive CAGR to deposits and withdrawals.','CAGR = (end/start)^(1/years) − 1'),
('Benchmark fit','Compare similar exposures and the same dates.','A bond-heavy portfolio differs from an all-stock index.','Use a relevant total-return benchmark.','Excess return = portfolio return − benchmark return'),
('Risk-adjusted assessment','Returns must be evaluated with risk and costs.','High leverage can increase both returns and losses.','Review drawdown and concentration alongside return.','Sharpe = (mean return − risk-free rate) / volatility')],
'Why can a high return still indicate poor portfolio management?','It may come from excessive concentration, leverage or luck that is unsuitable for the goal.'),
('🧠 Behavior & decision discipline','Advanced','Risk',[
('FOMO','Recent winners can tempt performance chasing.','Buying after viral attention without a thesis.','Use a written checklist and cooling-off period.','Rule adherence; turnover'),
('Anchoring','Purchase price can distort current assessment.','Waiting to break even despite a broken thesis.','Reassess future prospects and opportunity cost.','Current risk and expected outcome'),
('Review cadence','Frequent checking can encourage unnecessary trades.','Daily reactions to ordinary volatility.','Separate scheduled reviews from material thesis changes.','Review frequency; transaction costs')],
'Should the original purchase price determine whether to hold?','It matters for tax and records, but future prospects, risk and alternatives drive the investment decision.'),
('🧯 Options, margin & leverage','Advanced','Leverage',[
('Margin','Borrowing magnifies exposure and creates interest and liquidation risks.','A broker can require more collateral after losses.','Understand possible losses beyond the initial cash.','Leverage = gross exposure / equity'),
('Options','Contract payoff depends on direction, timing and volatility.','A call expires worthless even if the company remains strong.','Distinguish a contract payoff from a stock thesis.','Call payoff = max(price − strike, 0) − premium'),
('Daily reset funds','Leveraged objectives often apply to one day.','Compounding makes a multi-day result path-dependent.','Read objectives before treating it as long-term exposure.','Daily target multiple ≠ holding-period multiple')],
'Does a 2× daily ETF guarantee twice a 1-year index return?','No. Daily resetting, compounding, fees and tracking effects change multi-day results.'),
('🛡️ Fraud & research quality','Advanced','BrokerCheck',[
('Registration checks','Verify professionals and firms independently.','An impersonator copies a legitimate company name.','Use regulator databases and verified contact details.','Registration record; disciplinary disclosures'),
('Claim quality','Guaranteed high returns and urgency are red flags.','A private message promises risk-free stock profits.','Question incentives, evidence and liquidity.','No-return guarantee; source date'),
('Account security','Protect credentials and review activity.','A fake support request asks for an OTP.','Use MFA and independently access your broker.','Alerts; login protection; beneficiary review')],
'What should you do before sending money to an unfamiliar promoter?','Verify identity and registration independently; examine disclosures and never rely on a social-media profile alone.')
]
MISTAKES=[
('Chasing hot stocks','Recency bias and FOMO','Use a thesis, valuation range and allocation rule','Investment journal; scheduled review'),
('Employer-stock concentration','Familiarity and default award accumulation','Measure exposure alongside job risk','Portfolio weights dashboard'),
('Ignoring costs','Small percentages look harmless','Inspect fund fees, spreads and recurring charges','Fee-drag calculator; prospectus'),
('Treating yield as guaranteed profit','Confusing distribution with return','Assess total return and payout sustainability','Dividend and cash-flow worksheet'),
('Trading before reading filings','Headlines are easier than statements','Read business, risks, statements and MD&A','SEC EDGAR'),
('Selling on every market decline','No written plan or liquidity reserve','Match allocation to risk capacity','Policy statement; reminders'),
('Using leverage without downside modeling','Focus on upside only','Model liquidation, interest and loss scenarios','Stress-test calculator'),
('Mishandling equity-award basis','Broker forms and compensation are separate','Reconcile plan documents and tax records','Basis ledger; qualified tax adviser')]
ISSUES=[
('Need cash during a downturn','Near-term cash mixed with volatile assets','Separate liquidity by time horizon','Goal buckets; cash-flow calendar'),
('Portfolio feels diversified but is not','Overlapping funds and correlated industries','Inspect underlying holdings','Holdings spreadsheet'),
('Unable to judge business quality','Incomplete statements or noisy metrics','Review earnings, cash, debt and competitive risks','10-K research template'),
('Taxes surprise after a sale','Missing dates, basis and account context','Estimate consequences before a transaction','Tax-lot ledger'),
('Returns difficult to interpret','Deposits mixed with performance','Use cash-flow-aware return calculations','Broker performance report'),
('Frequent changes hurt consistency','Unclear review rules','Set review cadence and thesis triggers','Decision checklist')]
