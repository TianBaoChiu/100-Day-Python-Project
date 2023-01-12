from menu import MENU
import time
import os


db = MENU

store = {
    'Water': 300,
    'Milk': 200,
    'Coffee': 100,
    'Money': 0,
    'Warning': False
}


def current_store(store):
    """
    打印出當前材料庫存，依照項目的順序打印

    Args:
        store (dic) : 當前材料的庫存

    Return:
        無
    """

    print(f"Water : {store['Water']} ml")
    print(f"Milk : {store['Milk']} ml")
    print(f"Coffee : {store['Coffee']} g")
    print(f"Money : $ {store['Money']}")


def materials_needs(db, goods):
    """
    根據商品名，回傳對應需要的材料以及成本

    Args:
        db (dic) : 商品的成分表
        goods (str) : user指定的商品

    Return:
        water (int) : 水的需求量
        milk (int) : 牛奶的需求量
        coffee (int) : 咖啡的需求量
        cost (int) :需要收取的金額
    """

    water = milk = coffee = cost = 0
    ingredients = db[goods]['ingredients']
    if 'water' in ingredients:
        water = ingredients['water']
    if 'milk' in ingredients:
        milk = ingredients['milk']
    if 'coffee' in ingredients:
        coffee = ingredients['coffee']
    cost = db[goods]['cost']
    print(f"Water : {water} ml")
    print(f"Milk : {milk} ml")
    print(f"Coffee : {coffee} g")
    print(f"Cost : $ {cost}")
    return water, milk, coffee, cost


def check_resources(store, water, milk, coffee):
    """
    檢查當前庫存是否可以製作當前飲品

    Args:
        store (dic) : 庫存
        water (int) :製作飲品所需材料
        milk (int) :製作飲品所需材料
        coffee (int) :製作飲品所需材料

    Return:
        result (bool) :是否可以製作
    """
    not_enough = []

    if (store['Water'] > water) and (store['Milk'] > milk) and (store['Coffee'] > coffee):
        result = True
        print("原料充足")
    else:
        result = False
        if (store['Water'] < water) and (water != 0):
            not_enough.append('water')
        if (store['Milk'] < milk) and (milk != 0):
            not_enough.append('milk')
        if (store['Coffee'] < coffee) and (coffee != 0):
            not_enough.append('coffee')

    if result == False:
        for i in not_enough:
            print(f"Sorry there is not enough {i}")

    return result


def process_coins():
    """
    讓用戶輸入欲投入金額並且換算
    """
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    print(f"共投入: {total} 元")
    return total


def re_the_store(store, water, milk, coffee, cost):
    """
    透過耗材更新儲存庫的值

    Args:
        store (dic) : 庫存
        water (int) :製作所需資源
        milk (int) :製作所需資源
        coffee (int) :製作所需資源
        cost (int) :賺到的錢
    Return:
        store (dic) :更新後的庫存

    """
    store['Water'] -= water
    store['Milk'] -= milk
    store['Coffee'] -= coffee
    store['Money'] += cost
    return store


def main():
    global store
    os.system('cls')
    Work = True
    while Work == True:
        user_input = input(
            "What would you like? (espresso/latte/cappuccino)").lower()
        if user_input == 'espresso':
            water, milk, coffee, cost = materials_needs(db, 'espresso')
        elif user_input == 'latte':
            water, milk, coffee, cost = materials_needs(db, 'latte')
        elif user_input == 'cappuccino':
            water, milk, coffee, cost = materials_needs(db, 'cappuccino')
        elif user_input == 'report':
            current_store(store)
            time.sleep(5)
            break
        elif user_input == 'off':
            print("Turn off the coffee machine...")
            time.sleep(5)
            break
        else:
            print("Wrong input")
            time.sleep(5)
            break
        print(f"Need {cost} dollars...")
        result = check_resources(store, water, milk, coffee)
        if result != True:
            store['Warning'] = True
            print("End the machine...")
            time.sleep(5)
            break
        total = process_coins()
        if total < cost:
            print("Sorry that's not enough money. Money refunded.")
            time.sleep(5)
            break

        if total > cost:
            print(f"Here is ${round(total-cost, 2)} dollars in change. ")

        store = re_the_store(store, water, milk, coffee, cost)

        print("Making your coffee...  Please wait a minute...")
        time.sleep(3)
        print(f"Here is your {user_input}")
        time.sleep(5)
        os.system('cls')


while store['Warning'] != True:
    main()
print("請補貨")
