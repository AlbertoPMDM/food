from src.database.database import Foods, Ingredients
import csv

class Foodlist:
    
    def __init__(self,l:list) -> None:
        self._menu:dict = Foodlist.makeMenu(l)
        print(self._menu)
        self._list:dict = Foodlist.makeList(l)
        print(self._list)
        self._est_total:float = Foodlist.makeEstTotal(self._list)
        print(self._est_total)

    def makeMenu(l:list) -> dict:
        '''
        Returns a dict with the total servings for each entry in the list, if an 
        entry is repeated, it adds up the servings
        '''
        tmp_menu={}
        for item in l:
            tmp = Foods.by_name(item)
            if item in tmp_menu:
                tmp_menu[item] += tmp['servings']
            elif item not in tmp_menu:
                tmp_menu[item] = tmp['servings']
        return tmp_menu

    def makeList(l:list) -> dict:
        '''
        Returns a dict of the ingredients for each entry with the ammount, the unit, the price_per_unit as total,
        and the price_per_unit as price, if ingredients are repeated, it adds up the ammount and price_per_ammount
        '''
        tmp_list = {}
        for item in l:
            tmp_ing_list = Foods.query_ingredients(item)
            for ingredient in tmp_ing_list:
                tmp_ing = Ingredients.by_id(ingredient['ingredient_id'])
                if tmp_ing['ingredient'] in tmp_list:
                    tmp_list[tmp_ing['ingredient']]['ammount'] += ingredient['ammount']
                    tmp_list[tmp_ing['ingredient']]['total'] += ingredient['price_per_ammount']
                elif tmp_ing['ingredient'] not in tmp_list:
                    tmp_list[tmp_ing['ingredient']] = {'ammount':ingredient['ammount']}
                    tmp_list[tmp_ing['ingredient']]['unit'] = tmp_ing['unit']
                    tmp_list[tmp_ing['ingredient']]['total'] = ingredient['price_per_ammount']
                    tmp_list[tmp_ing['ingredient']]['price'] = tmp_ing['price_per_unit']
        return tmp_list

    def makeEstTotal(d:dict) -> float:
        '''
        Returns the estimated total for a given list made with makeList, from this class
        '''
        tmp_est_total:float = 0.0
        for key in d:
            tmp_est_total += d[key]['total']

        return tmp_est_total

    def export(self) -> None:
        with open('foodlist.csv', 'w', newline='') as csvfile:

            spamwriter = csv.writer(csvfile)

            spamwriter.writerow(['Menu'])
            spamwriter.writerow(['food', 'servings'])
            for key, item in self._menu.items():
                spamwriter.writerow([key, item])

            spamwriter.writerow([])
            spamwriter.writerow(['List'])
            spamwriter.writerow(['stock', 'item', 'ammount', 'unit', 'total', 'price'])
            for key, item in self._list.items():
                spamwriter.writerow(['', key, item['ammount'], item['unit'], item['total'], item['price']])
                
            spamwriter.writerow([])
            spamwriter.writerow(['Est. Total'])
            spamwriter.writerow([self._est_total])