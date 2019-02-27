html='''
<div class='panel'>
<div class='panel-heading'>
<h4>Hello</h4>
</div>
<div class='panel-body'>
<ul class='list' id='list-1'>
<li class='element'>Foo</li>
<li class='element'>Bar</li>
<li class='element'>Jay</li>
</ul>
<ul class='list list-small' id='list-2'>
<li class='element'>Foo</li>
<li class='element'>Bar</li>
</ul>
</div>
</div>
'''
from bs4 import BeautifulSoup

soup=BeautifulSoup(html,'lxml')
'''print(soup.find_all('ul'))
print(type(soup.find_all(name='ul')[0]))
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
    for li in ul.find_all('li'):
        print(li.string)'''

#print(soup.find_all(attrs={'id':'list-1'}))
#print(soup.find_all(attrs={'class':'list list-small'}))

print(soup.find_all(id='list-1'))
#class是关键字，所以要加"_"
print(soup.find_all(class_='list'))