import pandas as pd
df=pd.DataFrame({'account_id':[1,2,3,4,5],'income':[50000,10000,2000,70000,5000]})
def account_rating(accounts:pd.DataFrame)->pd.DataFrame:
        salaries = pd.DataFrame({
        'category':['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count':[
        accounts[accounts['income'] < 20000].shape[0],
        accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0],
        accounts[accounts['income'] > 50000].shape[0]]
        })
        salaries.drop_duplicates()
        return salaries
print(df.shape)
# category=['Low Salary','Average Salary','High Salary']
# df2=pd.DataFrame({'category':category})
# def account_rating(accounts:pd.DataFrame)->pd.DataFrame:
#     accounts['category']=accounts['income'].apply(get_category)
#     df3=accounts.groupby('category').size().to_frame()
#     #pd.merge(df2,df3,'left',left_on='category',right_on='category')
#     return pd.merge(df2,df3,'left',left_on='category',right_on='category').fillna(0)

# def get_category(income):
#     if income<20000:
#         return category[0]
#     elif income in range(20000,50000):
#         return category[1]
#     elif income>50000:
#         return category[2]
        

print(account_rating(df))