# Analyzing the Relationship Between GDP, Public Education Expenditure,and Illiteracy Rates, Education Level, and Economic Activity Participation in Brazil, Colombia and Peru (2002–2020)
![Project Image](https://github.com/canberkarc/education-and-americas/tree/main/project/image.jpg)
Reference: Image by [Steve Buissinne](https://pixabay.com/users/stevepb-282134/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=948603) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=948603)

This project examines how GDP and public expenditure on education correlate with key educational outcomes in Brazil, 
Colombia, and Peru between 2002 and 2020. The data has key indicators related to economic performance and education, 
and is good for deriving meaningful insights and conducting cross-country analyses.
Focusing on illiteracy rates, the population with 13 or more years of education, and their economic activity participation, 
to explore the effect of economic factors on educational opportunities and outcomes.

## Repository's Tree
```
education-and-americas/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── exercise-feedback.yml
├── data/
├── examples/
├── exercises/
│   ├── exercise1.jv
│   ├── exercise2.jv
│   ├── exercise3.jv
│   ├── exercise4.jv
│   ├── exercise5.jv
├── project/
│   ├── analysis-presentation.ipynb
│   ├── analysis-report.pdf
│   ├── analysis.ipynb
│   ├── data-report.pdf
│   ├── data_pipeline.py
│   ├── pipeline.sh
│   ├── project-plan.md
│   ├── requirements.txt
│   ├── tests.py
│   └── tests.sh
├── .gitignore
└── README.md
```

### Conclusion

• GDP plays an important role in educational progress, while improvement in education
access is needed in Brazil, Colombia, and Peru.
• Public expenditure on education appears to help reduce illiteracy and facilitate increased
funding for education but in Colombia, there seems to be possible inefficiencies in
education funding.
• A higher GDP does not always have a positive impact on education funding.
• While GDP and public expenditure on education positively correlate in Peru, Public
Expenditure on Education shows fluctuations, suggesting that there may be challenges in
sustaining education funding despite GDP growth.
• Population with higher levels of education is associated with higher rates of economic
participation in all three countries.

This study has limitations such as the absence of regional differences in education spending and other socio-economic factors that may influence educational outcomes.
Therefore further research is needed, incorporating additional factors that influence educational opportunities and outcomes.

### Usage
Execute the data processing part by running pipeline.sh to get the data for the analysis. The data pipeline can be tested using tests.sh.

### Licenses
The code included in this project is under MIT license. 

License descriptions of the data sources used in this project are given below:

1. World Bank Data Catalog
* License: CC-BY 4.0
* Attribution: “The World Bank: The World Bank Data Catalog under the CC-BY 4.0 License.”
* https://datacatalog.worldbank.org/public-licenses

2. CEPAL Statistics
* License: For educational and non-commercial use.
* Attribution: “Economic Commission for Latin America and the Caribbean (ECLAC), CEPALSTAT.”
* https://statistics.cepal.org/portal/cepalstat/open-data.html
