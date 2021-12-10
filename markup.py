from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


mainAll=KeyboardButton('Все новости')
mainFinance=KeyboardButton('Финансы')
mainFamily=KeyboardButton('Семья')
mainPolitics=KeyboardButton('Политика')
mainWorld=KeyboardButton('Мир')
mainBusiness=KeyboardButton('Шоубизнес')
mainSocity=KeyboardButton('Общество')
mainSpecial=KeyboardButton('Спецпроекты')
mainMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(mainAll,mainFinance,mainFamily,mainPolitics,mainWorld,mainBusiness,mainSocity,mainSpecial)


financeBank=KeyboardButton('Банки')
financeInsurance=KeyboardButton('Страхование')
financePension=KeyboardButton('Пенсии и пособия')
financeEconomy=KeyboardButton('Экономика')
financeTrade=KeyboardButton('Фондовый рынок')
financeOwn=KeyboardButton('Личные финансы')
financeReiting=KeyboardButton('Рейтинг Нурфин')
btnMain=KeyboardButton('Главное')
financeMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(financeBank,financeInsurance,financePension,financeEconomy,financeTrade,financeOwn,financeReiting,btnMain)

familyPopular=KeyboardButton('Популярное')
familyRelation=KeyboardButton('Отношения')
familyBaby=KeyboardButton('Дети')
familyGl=KeyboardButton('Глянец')
familyBeuty=KeyboardButton('Красота')
familyOwn=KeyboardButton('Самореализация')
familyMenu=ReplyKeyboardMarkup(resize_keyboard=True).add(familyPopular,familyRelation,familyBaby,familyGl,familyBeuty,familyOwn,btnMain)


today=KeyboardButton('Сегодня')
yesterday=KeyboardButton('Вчера')
dayBtn=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(today,yesterday,btnMain)





