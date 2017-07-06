import re

string = "Lorem ipsum ftp://link.sample dolor sit amet https://www.lorem.com/ipsum.php?q=suas, nusquam tincidunt ex per, ius modus integre no, quando utroque placerat qui no. Mea conclusionemque vituperatoribus et, omnes malorum est id, pri omnes atomorum expetenda ex. Elit pertinacia no eos, nonumy comprehensam id mei. Ei eum maiestatis quaerendum https://www.lorem.org😀. Pri posse constituam in, sit http://news.bbc.co.uk omnium assentior definitionem ei. Cu duo equidem meliore qualisque."

result = re.findall(r"(?:ftp|http|https)://(?:www)?.\w+\.\w+/?[\w\.\?=#]*", string)
print(result)