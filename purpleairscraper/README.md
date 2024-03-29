# Scraping PurpleAir sensors

A quick sketch of something I might use elsewhere.

This applies the 2021 correction for fire and smoke,
and is giving me slightly higher numbers than PurpleAir's conversion.
I've double-checked the math.

TODO: Triple-check the math.

## Setup

Copy `env.template` to `.env` and fill it in with PurpleAir API keys.

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt

Then, to scape data

    ./purpleair.py SENSOR_ID > data.json

If the JSON returned from the PurpleAir API does not contain an 'error' key,
the 'sensor' block is augmented with a few new keys.

  * 'aqi' is derived per the AirNow table
  * 'category' comes from the AirNow table
  * 'category\_color' is from elsewhere in the AirNow document

## References

  * [PurpleAir API documentation](https://community.purpleair.com/t/making-api-calls-with-the-purpleair-api/180)
  * [Technical Assistance Document for the
Reporting of Daily Air Quality – the Air Quality
Index (AQI)](https://www.airnow.gov/sites/default/files/2021-05/aqi-technical-assistance-document-sept2018.pdf)
  * [Sensor data cleaning and correction: Application on the AirNow Fire and Smoke Map](https://cfpub.epa.gov/si/si_public_record_report.cfm?dirEntryId=353088&Lab=CEMM)
