## Scrapper for Encumbrance Certificates

![](capture.gif)

This uses selenium to get encumbrance certificates from [here](https://tnreginet.gov.in/portal/?UserLocaleID=en).

## How to run?

Create a new environment using `requirements.txt`. Then run `main.py`. This accepts following commandline args

- sro_office
- doc_number
- year
- doc_type

Example command to run

```shell
python main.py --sro_office=Aandimadam --doc_number=10 --year=2022 --doc_type="Regular Document"
```

## Project Structure
- constants.py: This contains css selectors for relevant tags
- utils.py: This contains functions to navigate through pages and do form submission
- main.py: Entry point to the application



