import requests
from bs4 import BeautifulSoup
import os

def scrape_and_save(url, output_dir):
    # Create directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Fetch webpage content
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title and text from the webpage
        title = soup.find("h1", class_="entry-title").text
        paragraph = soup.find("div", class_="td-post-content tagdiv-type").get_text()
        
        # Construct filename from the title (cleaned up for file system)
        filename = "".join([c for c in title if c.isalpha() or c.isdigit()]).rstrip() + ".txt"
        
        # Write title and paragraph to file
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as file:
            file.write(f"Title: {title}\n\n")
            file.write(f"Paragraph:\n{paragraph}")
        print(f"Saved content from {url} to {filename}")
    else:
        print(f"Failed to retrieve content from {url}")

def main():
    urls = [
        "https://insights.blackcoffer.com/ml-and-ai-based-insurance-premium-model-to-predict-premium-to-be-charged-by-the-insurance-company/",
    "https://insights.blackcoffer.com/streamlined-integration-interactive-brokers-api-with-python-for-desktop-trading-application/",
    "https://insights.blackcoffer.com/efficient-data-integration-and-user-friendly-interface-development-navigating-challenges-in-web-application-deployment/",
    "https://insights.blackcoffer.com/effective-management-of-social-media-data-extraction-strategies-for-authentication-security-and-reliability/",
    "https://insights.blackcoffer.com/streamlined-trading-operations-interface-for-metatrader-4-empowering-efficient-management-and-monitoring/",
    "https://insights.blackcoffer.com/efficient-aws-infrastructure-setup-and-management-addressing-security-scalability-and-compliance/",
    "https://insights.blackcoffer.com/streamlined-equity-waterfall-calculation-and-deal-management-system/",
    "https://insights.blackcoffer.com/automated-orthopedic-case-report-generation-harnessing-web-scraping-and-ai-integration/",
    "https://insights.blackcoffer.com/streamlining-time-calculation-in-warehouse-management-leveraging-shiphero-api-and-google-bigquery-integration/",
    "https://insights.blackcoffer.com/efficient-database-design-and-management-streamlining-access-and-integration-for-partner-entity-management/",
    "https://insights.blackcoffer.com/automated-campaign-management-system-a-comprehensive-solution-with-linkedin-and-email-integration/",
    "https://insights.blackcoffer.com/ai-driven-data-analysis-ai-tool-using-langchain-for-a-leading-real-estate-and-financing-firm-worldwide/",
    "https://insights.blackcoffer.com/grafana-dashboard-to-visualize-and-analyze-sensors-data/",
    "https://insights.blackcoffer.com/mvp-for-a-software-that-analyses-content-from-audio-pharma-based/",
    "https://insights.blackcoffer.com/data-engineering-and-management-tool-airbyte-with-custom-data-connectors-to-manage-crm-database/",
    "https://insights.blackcoffer.com/text-summarizing-tool-to-scrape-and-summarize-pubmed-medical-papers/",
    "https://insights.blackcoffer.com/7up7down-10updown-snakes-and-ladder-games-built-using-oops/",
    "https://insights.blackcoffer.com/data-studio-dashboard-with-a-data-pipeline-tool-synced-with-podio-using-custom-webhooks-and-google-cloud-function/",
    "https://insights.blackcoffer.com/end-to-end-tool-to-optimize-routing-and-planning-of-field-engineers-using-googles-cvrp-tw-algorithm/",
    "https://insights.blackcoffer.com/end-to-end-tool-to-predict-biofuel-prices-using-ieso-data/",
    "https://insights.blackcoffer.com/etl-discovery-tool-using-llma-langchain-openai/",
    "https://insights.blackcoffer.com/gpt-ocr-api/",
    "https://insights.blackcoffer.com/dockerize-the-aws-lambda-for-serverless-architecture/",
    "https://insights.blackcoffer.com/design-and-develop-a-product-recommendation-engine-based-on-the-features-of-products/",
    "https://insights.blackcoffer.com/database-discovery-tool-using-openai/",
    "https://insights.blackcoffer.com/automate-the-data-management-process/",
    "https://insights.blackcoffer.com/realtime-kibana-dashboard-for-a-financial-tech-firm/",
    "https://insights.blackcoffer.com/data-management-etl-and-data-automation/",
    "https://insights.blackcoffer.com/data-management-egeas/",
    "https://insights.blackcoffer.com/design-and-develop-powershell-script/",
    "https://insights.blackcoffer.com/design-and-develop-jenkins-shared-library/",
    "https://insights.blackcoffer.com/design-and-develop-retool-app-for-wholecell-io-and-asana-data-using-their-apis/",
    "https://insights.blackcoffer.com/design-and-develop-a-retool-app-that-will-show-stock-and-crypto-related-information-using-iex-api/",
    "https://insights.blackcoffer.com/crm-monday-com-make-com-to-data-warehouse-to-klipfolio-dashboard/",
    "https://insights.blackcoffer.com/ner-task-using-bert-with-data-in-xml-format/",
    "https://insights.blackcoffer.com/qualtrics-api-integration-using-python/",
    "https://insights.blackcoffer.com/design-and-develop-mlops-framework-for-data-centric-ai/",
    "https://insights.blackcoffer.com/nlp-based-approach-for-data-transformation/",
    "https://insights.blackcoffer.com/an-etl-tool-to-pull-data-from-shiphero-to-google-bigquery-data-warehouse/",
    "https://insights.blackcoffer.com/plaid-financial-analytics-a-data-driven-dashboard-to-generate-insights/",
    "https://insights.blackcoffer.com/recommendation-engine-for-insurance-sector-to-expand-business-in-the-rural-area/",
    "https://insights.blackcoffer.com/data-from-crm-via-zapier-to-google-sheets-dynamic-to-powerbi/",
    "https://insights.blackcoffer.com/data-warehouse-to-google-data-studio-looker-dashboard/",
    "https://insights.blackcoffer.com/crm-monday-com-via-zapier-to-power-bi-dashboard/",
    "https://insights.blackcoffer.com/monday-com-to-kpi-dashboard-to-manage-view-and-generate-insights-from-the-crm-data/",
    "https://insights.blackcoffer.com/data-management-for-a-political-saas-application/",
    "https://insights.blackcoffer.com/google-lsa-ads-google-local-service-ads-etl-tools-and-dashboards/",
    "https://insights.blackcoffer.com/ad-networks-marketing-campaign-data-dashboard-in-looker-google-data-studio/",
    "https://insights.blackcoffer.com/analytical-solution-for-a-tech-firm/",
    "https://insights.blackcoffer.com/ai-solution-for-a-technology-information-and-internet-firm/",
    "https://insights.blackcoffer.com/ai-and-nlp-based-solutions-to-automate-data-discovery-for-venture-capital-and-private-equity-principals/",
    "https://insights.blackcoffer.com/an-etl-solution-for-an-internet-publishing-firm/",
    "https://insights.blackcoffer.com/ai-based-algorithmic-trading-bot-for-forex/",
    "https://insights.blackcoffer.com/equity-waterfalls-model-based-saas-application-for-real-estate-sector/",
    "https://insights.blackcoffer.com/ai-solutions-for-foreign-exchange-an-automated-algo-trading-tool/",
    "https://insights.blackcoffer.com/ai-agent-development-and-deployment-in-jina-ai/",
    "https://insights.blackcoffer.com/golden-record-a-knowledge-graph-database-approach-to-unfold-discovery-using-neo4j/",
    "https://insights.blackcoffer.com/advanced-ai-for-trading-automation/",
    "https://insights.blackcoffer.com/create-a-knowledge-graph-to-provide-real-time-analytics-recommendations-and-a-single-source-of-truth/",
    "https://insights.blackcoffer.com/advanced-ai-for-thermal-person-detection/",
    "https://insights.blackcoffer.com/advanced-ai-for-road-cam-threat-detection/",
    "https://insights.blackcoffer.com/advanced-ai-for-pedestrian-crossing-safety/",
    "https://insights.blackcoffer.com/handgun-detection-using-yolo/",
    "https://insights.blackcoffer.com/using-graph-technology-to-create-single-customer-view/",
    "https://insights.blackcoffer.com/car-detection-in-satellite-images/",
    "https://insights.blackcoffer.com/building-a-physics-informed-neural-network-for-circuit-evaluation/",
    "https://insights.blackcoffer.com/connecting-mongodb-database-to-power-bi-dashboard-dashboard-automation/",
    "https://insights.blackcoffer.com/data-transformation/",
    "https://insights.blackcoffer.com/e-commerce-store-analysis-purchase-behavior-ad-spend-conversion-traffic-etc/",
    "https://insights.blackcoffer.com/kpi-dashboard-for-accountants/",
    "https://insights.blackcoffer.com/return-on-advertising-spend-dashboard-marketing-automation-and-analytics-using-etl-and-dashboard/",
    "https://insights.blackcoffer.com/ranking-customer-behaviours-for-business-strategy/",
    "https://insights.blackcoffer.com/algorithmic-trading-for-multiple-commodities-markets-like-forex-metals-energy-etc/",
    "https://insights.blackcoffer.com/trading-bot-for-forex/",
    "https://insights.blackcoffer.com/python-model-for-the-analysis-of-sector-specific-stock-etfs-for-investment-purposes%ef%bf%bc/",
    "https://insights.blackcoffer.com/medical-classification/",
    "https://insights.blackcoffer.com/design-develop-bert-question-answering-model-explanations-with-visulization/"
    "https://insights.blackcoffer.com/design-and-develop-solution-to-anomaly-detection-classification-problems/",
"https://insights.blackcoffer.com/an-etl-solution-for-currency-data-to-google-big-query/",
"https://insights.blackcoffer.com/etl-and-mlops-infrastructure-for-blockchain-analytics/",
"https://insights.blackcoffer.com/an-agent-based-model-of-a-virtual-power-plant-vpp/",
"https://insights.blackcoffer.com/transform-api-into-sdk-library-and-widget/",
"https://insights.blackcoffer.com/integration-of-a-product-to-a-cloud-based-crm-platform/",
"https://insights.blackcoffer.com/a-web-based-dashboard-for-the-filtered-data-retrieval-of-land-records/",
"https://insights.blackcoffer.com/integration-of-video-conferencing-data-to-the-existing-web-app/",
"https://insights.blackcoffer.com/design-develop-an-app-in-retool-which-shows-the-progress-of-the-added-video/",
"https://insights.blackcoffer.com/auvik-connectwise-integration-in-grafana/",
"https://insights.blackcoffer.com/data-integration-and-big-data-performance-using-elk-stack/",
"https://insights.blackcoffer.com/web-data-connector/",
"https://insights.blackcoffer.com/an-app-for-updating-the-email-id-of-the-user-and-stripe-refund-tool-using-retool/",
"https://insights.blackcoffer.com/an-ai-ml-based-web-application-that-detects-the-correctness-of-text-in-a-given-video/",
"https://insights.blackcoffer.com/website-tracking-and-insights-using-google-analytics-google-tag-manager/",
"https://insights.blackcoffer.com/dashboard-to-track-the-analytics-of-the-website-using-google-analytics-and-google-tag-manager/",
"https://insights.blackcoffer.com/power-bi-dashboard-on-operations-transactions-and-marketing-embedding-the-dashboard-to-web-app/",
"https://insights.blackcoffer.com/nft-data-automation-looksrare-and-etl-tool/",
"https://insights.blackcoffer.com/optimize-the-data-scraper-program-to-easily-accommodate-large-files-and-solve-oom-errors/",
"https://insights.blackcoffer.com/making-a-robust-way-to-sync-data-from-airtables-to-mongodb-using-python-etl-solution/",
"https://insights.blackcoffer.com/incident-duration-prediction-infrastructure-and-real-estate/",
"https://insights.blackcoffer.com/statistical-data-analysis-of-reinforced-concrete/",
"https://insights.blackcoffer.com/database-normalization-segmentation-with-google-data-studio-dashboard-insights/",
"https://insights.blackcoffer.com/power-bi-dashboard-to-drive-insights-from-complex-data-to-generate-business-insights/",
"https://insights.blackcoffer.com/real-time-dashboard-to-monitor-infrastructure-activity-and-machines/",
"https://insights.blackcoffer.com/electric-vehicles-ev-load-management-system-to-forecast-energy-demand/",
"https://insights.blackcoffer.com/power-bi-data-driven-map-dashboard/",
"https://insights.blackcoffer.com/google-local-service-ads-lsa-leads-dashboard/",
"https://insights.blackcoffer.com/aws-lex-voice-and-chatbot/",
"https://insights.blackcoffer.com/metabridges-api-decentraland-integration/",
"https://insights.blackcoffer.com/microsoft-azure-chatbot-with-luis-language-understanding/",
"https://insights.blackcoffer.com/impact-of-news-media-and-press-on-innovation-startups-and-investments/",
"https://insights.blackcoffer.com/aws-quicksight-reporting-dashboard/",
"https://insights.blackcoffer.com/google-data-studio-dashboard-for-marketing-ads-and-traction-data/",
"https://insights.blackcoffer.com/gangala-in-e-commerce-big-data-etl-elt-solution-and-data-warehouse/",
"https://insights.blackcoffer.com/big-data-solution-to-an-online-multivendor-marketplace-ecommerce-business/",
"https://insights.blackcoffer.com/creating-a-custom-report-and-dashboard-using-the-data-got-from-atera-api/",
"https://insights.blackcoffer.com/azure-data-lake-and-power-bi-dashboard/",
"https://insights.blackcoffer.com/google-data-studio-pipeline-with-gcp-mysql/",
"https://insights.blackcoffer.com/quickbooks-dashboard-to-find-patterns-in-finance-sales-and-forecasts/",
"https://insights.blackcoffer.com/marketing-sales-and-financial-data-business-dashboard-wink-report/",
"https://insights.blackcoffer.com/react-native-apps-in-the-development-portfolio/",
"https://insights.blackcoffer.com/a-leading-firm-website-seo-optimization/",
"https://insights.blackcoffer.com/a-leading-hospitality-firm-in-the-usa-website-seo-optimization/",
"https://insights.blackcoffer.com/a-leading-firm-in-the-usa-website-seo-optimization/",
"https://insights.blackcoffer.com/a-leading-musical-instrumental-website-seo-optimization/",
"https://insights.blackcoffer.com/a-leading-firm-in-the-usa-seo-and-website-optimization/",
"https://insights.blackcoffer.com/immigration-datawarehouse-ai-based-recommendations/",
"https://insights.blackcoffer.com/lipsync-automation-for-celebrities-and-influencers/",
"https://insights.blackcoffer.com/key-audit-matters-predictive-modeling/",
"https://insights.blackcoffer.com/splitting-of-songs-into-its-vocals-and-instrumental/",
"https://insights.blackcoffer.com/ai-and-ml-technologies-to-evaluate-learning-assessments/",
"https://insights.blackcoffer.com/datawarehouse-and-recommendations-engine-for-airbnb/",
"https://insights.blackcoffer.com/real-estate-data-warehouse/",
"https://insights.blackcoffer.com/traction-dashboards-of-marketing-campaigns-and-posts/",
"https://insights.blackcoffer.com/google-local-service-ads-lsa-data-warehouse/",
"https://insights.blackcoffer.com/google-local-service-ads-missed-calls-and-messages-automation-tool/",
"https://insights.blackcoffer.com/marketing-ads-leads-call-status-data-tool-to-bigquery/",
"https://insights.blackcoffer.com/marketing-analytics-to-automate-leads-call-status-and-reporting/",
"https://insights.blackcoffer.com/callrail-analytics-leads-report-alert/",
"https://insights.blackcoffer.com/marketing-automation-tool-to-notify-lead-details-to-clients-over-email-and-phone/",
"https://insights.blackcoffer.com/data-etl-local-service-ads-leads-to-bigquery/",
"https://insights.blackcoffer.com/marbles-stimulation-using-python/",
"https://insights.blackcoffer.com/stocktwits-data-structurization/",
"https://insights.blackcoffer.com/sentimental-analysis-on-shareholder-letter-of-companies/",
"https://insights.blackcoffer.com/population-and-community-survey-of-america/",
"https://insights.blackcoffer.com/google-lsa-api-data-automation-and-dashboarding/",
"https://insights.blackcoffer.com/healthcare-data-analysis/",
"https://insights.blackcoffer.com/budget-sales-kpi-dashboard-using-power-bi/",
"https://insights.blackcoffer.com/amazon-buy-bot-an-automation-ai-tool-to-auto-checkouts/"
    ]
    
    output_directory = "scraped_content"
    
    for url in urls:
        scrape_and_save(url, output_directory)

if __name__ == "__main__":
    main()
