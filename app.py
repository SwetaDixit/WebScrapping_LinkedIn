import utils as utils
import streamlit as st
from io import StringIO
from datetime import datetime

def dataframe_to_csv_download(dataframe):
    # Convert the DataFrame to a CSV string
    csv = dataframe.to_csv(index=False)
    csv_bytes = csv.encode('utf-8')

    today = datetime.now().strftime("%Y-%m-%d_%H-%M")

    # Create a download button in the Streamlit app
    st.download_button(
        label="Download CSV File",
        data=csv_bytes,
        file_name=f"ScrappedData_{today}.csv",
        mime="text/csv",
    )

def main():
    st.title('LinkedIn Job Scraper')
    st.write('This app scrapes LinkedIn for job listings.')
    url = st.text_area("Enter the URL here..")

    if st.button("Get Records") and url:
        with st.spinner("Scraping the given URL..."):
            try:
                scrap_df = utils.scrap_data(url)
                st.dataframe(scrap_df)
                dataframe_to_csv_download(scrap_df)
                st.success("Scraping completed successfully!")
            except Exception as e:
                st.error(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    main()
