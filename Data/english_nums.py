a = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
     'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
     'seventeen', 'eighteen', 'nineteen']
    
b = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
     'ninety']


def word(n):
    num = ''
    if n==0:
        return 'zero'
    elif n < 0:
        return 'negative ' + word(-n)
    else:
        if n >= 1000:
            num += word(n//1000) + ' thousand'
            if 0 < n % 1000 < 100:
                num += ' and'
            n = n % 1000
        if n >= 100:
            num += ' ' + a[(n // 100)] + ' hundred'

            if n % 100 != 0:
                num += ' and'
        
        if n%100 < 20:
            num += ' ' + a[n%100]
        else:
            num += ' ' + b[(n%100)//10] + ' ' + a[n%10]
        
        return num.strip()

while True:
    n = int(input())
    print(word(n))