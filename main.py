from bs4 import BeautifulSoup
import requests
import pandas as pd
from matplotlib import pyplot as plt

p = []
t = []
time = []

myaddress = "https://www.bbc.com/turkce/haberler-dunya-55610937"

u = requests.get(myaddress)
u = u.content  # necessary

soup = BeautifulSoup(u, "html.parser")  # it is used to see the output better


y = soup.find_all("p", attrs={"class": "css-oywjep-GridComponent e57qer20"} and {
    "class": "css-1ikvhrr-Paragraph e1cc2ql70"})
z = soup.find_all("h1",
                  attrs={"class": "css-e19l8g-GridComponent e57qer20"} and {"class": "css-1jgs8so-Headline e1yj3cbb0"})

time_find = soup.find("time", attrs={"class": "e1j2237y1 css-vf19ca-GridComponent e57qer20"} and {
    "class": "css-1gpsqpy-StyledTimestamp e4zesg50"})
find_all_time = soup.find("time", attrs={"class": "e1j2237y3 css-1aoqp8k-GridComponent e57qer20"} and {
    "datetime": "2021-01-10"})
time.append(find_all_time.text)

#time.append(time_find.text)
# print(time_find.get("datetime") + " " + time_find.text)

# for title
for tit in z:
    # print(tit.text)
    tit = tit.text.split()
    for w in tit:
        t.append(w)

t.sort()
wdd = {}
for w in t:
    wdd[w] = t.count(w)
# end

# for the words

for item in y:
    # print(item.text)
    item = item.text.split()
    # print(item)
    for w in item:
        p.append(w)

p.sort()
# print(p)
wd = {}
for w in p:
    wd[w] = p.count(w)
# end

# DataFrame ploting

dff = pd.DataFrame(t)
plt.hist(t, rwidth=0.5)
plt.tight_layout()
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()

# DataFrame ploting
df = pd.DataFrame(p)
i = 15
plt.hist(p[:i])
j = len(p)
while i <= j:
    plt.hist(p[i:i * 2])
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    i = i * 2 + 1

plt.tight_layout()
plt.show()

# DataFrame ploting
dfff = pd.DataFrame(time)
plt.plot(time, marker=".")
plt.xlabel("Frequency")
plt.ylabel("Date")
plt.tight_layout()
plt.show()
# end
