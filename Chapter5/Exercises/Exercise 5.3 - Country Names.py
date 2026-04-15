"""
Exercise 5.3 Country Names

Given a list of countries as a list:

	1) Generate and print a new list that contains only the countries whose name has two or more words.
	For example, United States, would be an element in the new list.

	2) Generate a second list that only includes countries that start with the letter 'N'

	3) Generate a third list that includes countries that are in BOTH lists 1 and 2.

	4) Print the following:
	    - The lenght of list one (number of countries in that list - should be 37)
	    - All three lists

	    Example Output:
            - There are 37 countries with more than one word in their name.
            - ['United States', 'United Kingdom', 'South Africa', 'South Korea', 'North Korea', 'New Zealand', 'Saudi Arabia', 'Democratic Republic of the Congo', 'Republic of the Congo', 'Czech Republic', 'United Arab Emirates', 'Papua New Guinea', 'Sri Lanka', 'Costa Rica', 'Bosnia and Herzegovina', 'Dominican Republic', 'Vatican City', 'South Sudan', 'North Macedonia', 'Ivory Coast', 'El Salvador', 'Central African Republic', 'Trinidad and Tobago', 'San Marino', 'Sierra Leone', 'Federated States of Micronesia', 'Burkina Faso', 'Cape Verde', 'Equatorial Guinea', 'East Timor', 'Antigua and Barbuda', 'Solomon Islands', 'Saint Kitts and Nevis', 'Saint Lucia', 'Marshall Islands', 'Saint Vincent and the Grenadines', 'São Tomé and Príncipe']
            - ['Norway', 'North Korea', 'New Zealand', 'Netherlands', 'Niger', 'Nigeria', 'Nepal', 'North Macedonia', 'Nicaragua', 'Namibia', 'Nauru']
            - ['North Korea', 'New Zealand', 'North Macedonia']


"""
countries = ['United States', 'Russia', 'Canada', 'China', 'Mexico', 'Brazil', 'Italy', 'United Kingdom', 'Australia',
             'France', 'Germany', 'Spain', 'Japan', 'India', 'Egypt', 'Ireland', 'Iceland', 'Argentina', 'South Africa',
             'Portugal', 'Sweden', 'Chile', 'Norway', 'South Korea', 'Finland', 'Turkey', 'North Korea', 'Greece',
             'Iran', 'New Zealand', 'Poland', 'Iraq', 'Denmark', 'Madagascar', 'Peru', 'Switzerland', 'Cuba',
             'Netherlands', 'Pakistan', 'Mongolia', 'Saudi Arabia', 'Indonesia', 'Colombia', 'Austria', 'Ukraine',
             'Belgium', 'Niger', 'Thailand', 'Afghanistan', 'Vietnam', 'Morocco', 'Israel', 'Panama',
             'Democratic Republic of the Congo', 'Uruguay', 'Bolivia', 'Sudan', 'Venezuela', 'Republic of the Congo',
             'Kazakhstan', 'Philippines', 'Nigeria', 'Romania', 'Hungary', 'Paraguay', 'Nepal', 'Czech Republic',
             'Croatia', 'Algeria', 'Syria', 'Libya', 'Estonia', 'Yemen', 'Slovakia', 'Kenya', 'Somalia', 'Haiti',
             'United Arab Emirates', 'Latvia', 'Ethiopia', 'Lithuania', 'Malaysia', 'Jamaica', 'Papua New Guinea',
             'Sri Lanka', 'Ecuador', 'Dominica', 'Chad', 'Oman', 'Belarus', 'Bulgaria', 'Laos', 'Cambodia', 'Albania',
             'Jordan', 'Taiwan', 'Serbia', 'Luxembourg', 'Slovenia', 'Costa Rica', 'Bosnia and Herzegovina',
             'Uzbekistan', 'Bangladesh', 'Tunisia', 'Zimbabwe', 'Honduras', 'Myanmar', 'Guatemala', 'Georgia', 'Ghana',
             'Mali', 'Dominican Republic', 'Vatican City', 'Bahamas', 'Cyprus', 'South Sudan', 'North Macedonia',
             'Turkmenistan', 'Nicaragua', 'Angola', 'Qatar', 'Singapore', 'Ivory Coast', 'Armenia', 'Lebanon', 'Belize',
             'Tanzania', 'Malta', 'Uganda', 'El Salvador', 'Zambia', 'Fiji', 'Andorra', 'Guinea', 'Guyana', 'Moldova',
             'Azerbaijan', 'Botswana', 'Monaco', 'Bhutan', 'Montenegro', 'Namibia', 'Central African Republic', 'Kuwait',
             'Mozambique', 'Liberia', 'Liechtenstein', 'Suriname', 'Kosovo', 'Cameroon', 'Senegal', 'Rwanda', 'Togo',
             'Tajikistan', 'Lesotho', 'Trinidad and Tobago', 'Eritrea', 'Kyrgyzstan', 'Barbados', 'Eswatini',
             'San Marino', 'Maldives', 'Mauritania', 'Gambia', 'Malawi', 'Benin', 'Sierra Leone', 'Bahrain', 'Mauritius',
             'Djibouti', 'Gabon', 'Federated States of Micronesia', 'Seychelles', 'Tonga', 'Brunei', 'Burkina Faso',
             'Samoa', 'Cape Verde', 'Burundi', 'Equatorial Guinea', 'East Timor', 'Antigua and Barbuda',
             'Solomon Islands', 'Saint Kitts and Nevis', 'Saint Lucia', 'Guinea-Bissau', 'Vanuatu', 'Marshall Islands',
             'Tuvalu', 'Grenada', 'Kiribati', 'Saint Vincent and the Grenadines', 'Palau', 'Comoros', 'Nauru', 'São Tomé and Príncipe']
