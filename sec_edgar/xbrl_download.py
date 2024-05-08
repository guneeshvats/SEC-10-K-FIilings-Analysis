
from sec_api import ExtractorApi, XbrlApi

xbrlApi=XbrlApi("1b2067db5d9a8a8ed8450c3d3b7a3d1b53fa96e265e0d83f8a77c6305e32407b")

extractorApi= ExtractorApi(api_key="1b2067db5d9a8a8ed8450c3d3b7a3d1b53fa96e265e0d83f8a77c6305e32407b")
 


filing_urls = [
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000004962/000000496223000006/axp-20221231.htm",
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000004962/000000496222000008/axp-20211231.htm",
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000004962/000000496221000013/axp-20201231.htm"
]

for i, filing_url in enumerate(filing_urls, 1):
    section_text = extractorApi.get_section(filing_url, "1A", "text")
    xbrl_json=xbrlApi.xbrl_to_json(htm_url=filing_url)   
    result = [f"{key}: {value}\n" for key, value in xbrl_json["CoverPage"].items()]
    filename = f'D:/Usefull stuff/Georgia Tech/Project/RAG_sec/filings/AXP_filings_{i}.txt'
    
    with open(filename, 'w') as f:
        for item in result:
            f.write(item)
        f.write(section_text)
 
   
filing_urls_UNH = [
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000731766/000073176621000013/unh-20201231.htm",
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000731766/000073176622000008/unh-20211231.htm",
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000731766/000073176623000008/unh-20221231.htm"
]

for i, filing_url in enumerate(filing_urls_UNH, 1):
    section_text = extractorApi.get_section(filing_url, "1A", "text")
    xbrl_json=xbrlApi.xbrl_to_json(htm_url=filing_url)   
    result = [f"{key}: {value}\n" for key, value in xbrl_json["CoverPage"].items()]
    filename = f'D:/Usefull stuff/Georgia Tech/Project/RAG_sec/filings/UNH_filings_{i}.txt'
    with open(filename, 'w') as f:
        for item in result:
            f.write(item)
        f.write(section_text)
        
        

filing_urls_MSFT = [
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000789019/000156459020034944/msft-10k_20200630.htm",
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000789019/000156459021039151/msft-10k_20210630.htm",
    "https://www.sec.gov/ix?doc=/Archives/edgar/data/0000789019/000156459022026876/msft-10k_20220630.htm"
]

for i, filing_url in enumerate(filing_urls_MSFT, 1):
    section_text = extractorApi.get_section(filing_url, "1A", "text")
    xbrl_json=xbrlApi.xbrl_to_json(htm_url=filing_url)   
    result = [f"{key}: {value}\n" for key, value in xbrl_json["CoverPage"].items()]
    filename = f'D:/Usefull stuff/Georgia Tech/Project/RAG_sec/filings/MSFT_filings_{i}.txt'
    with open(filename, 'w') as f:
        for item in result:
            f.write(item)
        f.write(section_text)
