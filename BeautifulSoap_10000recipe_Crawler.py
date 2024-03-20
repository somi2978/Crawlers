from bs4 import BeautifulSoup  ## pip install beautifulsoup4
import urllib.request
import pandas as pd  ## pip install pandas
import datetime

#[CODE 1]
def Recipe10000(result):
    for page in range(1,3):  ## 1~2 페이지 추출
        Recipe_url ='https://www.10000recipe.com/issue/view.html?cid=gdubu33&types=magazine&page='+str(page)
        print(Recipe_url)
        html = urllib.request.urlopen(Recipe_url)
        soupRecipe=BeautifulSoup(html, 'html.parser')
        ThemeList = soupRecipe.find('div',attrs={'class':'theme_list'}) 
        for recipe in ThemeList.find_all('a',attrs={'class':'thumbnail'}):
            recipeThumbnail = recipe.find_all('img')[0].get("src")
            recipeTitle = recipe.find_all('span')[0].string

            result.append([recipeTitle]+[recipeThumbnail])

    return result

#[CODE 2]
def main():
    result=[]
    print('Recipe 10000 crawling start')
    Recipe10000(result)
    recipe_tbl = pd.DataFrame(result, columns = ('레시피 명','썸네일 이미지 url'))
    recipe_tbl.to_csv('./10000recipe.csv',encoding='cp949',mode='w',index=True)
    del result[:]

if __name__ == '__main__':
    main()

    
