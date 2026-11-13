# MPE Engineering Tools

A standalone Streamlit landing page for MPE engineering analysis tools. Each dashboard runs as an independent public Streamlit application.

## Configure links

Set the verified deployed URLs in app_links.toml under [apps]:

- load_flow
- frequency_sweep
- harmonics

Leave a value empty until its corresponding dashboard has been deployed and checked. The page shows a deployment placeholder while a URL is blank. Configured links use Streamlit's link button and open in a new browser tab.

## Run locally

    conda env create -f environment.yml
    conda activate mpe-engineering-tools
    streamlit run app.py

## Engineering review

The dashboards require specific input formats. A competent engineer must review results before using them in engineering decisions.

## Deployment

Deploy app.py from the main branch of this repository in Streamlit Community Cloud. Keep app_links.toml in the repository and set only verified live dashboard URLs.