---
name: portfolio-analysis
description: Analyzes a portfolio of stocks from a CSV file. Use this skill when the user provides a CSV with stock names, quantities, and acquisition prices and asks for a portfolio analysis, review, or buy/hold/sell decisions based on recent quarterly filings, valuation, growth, profitability, promoter holding, and dividends.
---

# Portfolio Analysis

## Overview

This skill analyzes a user's stock portfolio provided via a CSV file. It evaluates each stock based on recent quarterly filings, news, valuation, growth, profitability, promoter holding, and dividends, and provides a buy/hold/sell decision assuming the user is a high net worth individual (valuation > 5 Crore).

## Workflow

When the user asks to analyze their portfolio and provides a CSV file, follow these steps:

### 1. Parse the CSV File
Read the provided CSV file to extract the list of stocks, the number of shares held, and the acquisition price for each stock.

### 2. Analyze Each Stock
For every stock in the portfolio, use your search tools (or web search if available) to gather the following information:
- **Recent Quarterly Filings & News**: What are the latest financial results and significant news events?
- **Valuation vs Market Average**: Is the stock overvalued or undervalued compared to its peers/market average?
- **Growth**: Is the company showing revenue and earnings growth?
- **Profitability**: Is the company profitable? What are its margins?
- **Promoter Holding**: Explicitly mention if the stock has seen an increase or decrease in promoter holding recently.
- **Dividends**: Explicitly mention if the company has given dividends recently.

### 3. Provide a Decision
Based on the analysis, provide a **Buy / Hold / Sell** decision for each stock. 
*Crucial Context*: Assume the user is a high net worth individual (HNI) with a portfolio valuation greater than 5 Crore. This means the investment strategy should lean towards wealth preservation, stable growth, and risk management. 
- *Buy*: If the stock shows strong growth, profitability, reasonable valuation, increasing promoter holding, and consistent dividends.
- *Hold*: If the stock is stable but lacks strong growth catalysts, or is fairly valued.
- *Sell*: If the company is showing declining profitability, poor growth, decreasing promoter holding, or is significantly overvalued without justification.

### 4. Output Format
Present the analysis in a clear, structured format (e.g., Markdown). For each stock, include:
- **Stock Name**
- **Acquisition Details**: Quantity and Acquisition Price
- **Analysis**:
  - Quarterly Filings & News
  - Valuation vs Market Average
  - Growth & Profitability
  - Promoter Holding
  - Dividends
- **Decision**: Buy / Hold / Sell (with a brief justification based on the HNI persona)

## Guidelines
- Be explicit about promoter holding and dividends, as these are key indicators of company health and management confidence.
- Ensure the analysis reflects the HNI persona (valuation > 5 Crore), focusing on long-term stability.
