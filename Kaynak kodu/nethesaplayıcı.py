print("\n" * 50)
x = input('1.TYT  /  2.AYT (Sayısal) / 3.Branş Denemesi : ')

x = int(x)
print('\n' * 50)

if x == 1:
	print('\nTürkçe: ')
	print('-------------\n')

	x = input('Doğru Sayısı: ')

	y = input('Yanlış Sayısı: ')

	print('\n' * 50)

	z = (int(x) - (int(y)/4))

	print('')

	print('Sosyal: ')
	print('-------------')
	print(' ')

	a = input('Doğru Sayısı: ')

	b = input('Yanlış Sayısı: ')

	print('\n' * 50)

	a = int(a)

	b = int(b)

	c = (a - (b/4))


	print(' ')

	print('Matematik: ')
	print('-------------\n')

	d = input('Doğru Sayısı: ')

	e = input('Yanlış Sayısı: ')

	print('\n' * 50)

	d = int(d)

	e = int(e)

	f = (d - (e/4))

	print(' ')

	print('Fen Bilimleri: ')
	print('------------------')
	print(' ')


	g = input('Doğru Sayısı: ')

	h = input('Yanlış Sayısı: ')

	g = int(g)

	h = int(h)

	i = (g - (h/4))

	aaa = (z+i+f+c)
	aaa = str(aaa)

	z = str(z)
	i = str(i)
	f = str(f)
	c = str(c)
	print('\n' * 50)

	print ('Türkçe: ' + z + '\n')
	print ('Sosyal: ' + c + '\n')
	print ('Matematik: ' + f + '\n')
	print ('Fen Bilimleri: ' + i + '\n' * 2)
	print('Toplam net: '+ aaa + '\n' * 2 )
	input('\n\nÇıkmak için enter tuşuna bas.')

if x == 2:
	print('Matematik:\n-------------\n ')

	x = input('Doğru Sayısı: ')

	y = input('Yanlış Sayısı: ')

	print('\n' * 50)

	x = int(x)

	y = int(y)

	z = (x - (y/4))

	z = str(z)

	print('\n' * 2)
	print('Fen Bilimleri:\n-------------\n')

	a = input('Doğru Sayısı: ')

	b = input('Yanlış Sayısı: ')

	print('\n' * 50)

	c = (int(a) - (int(b)/4))

	print('\n' * 3)

	print('Matematik :' + str(z) + '\n')
	print('Fen Bilimleri:' + str(c) + '\n')
	aaa = (float(z) + float(c))
	print('Net: ' + str(aaa) + '\n' * 3)
	input('\n\nÇıkmak için enter tuşuna bas.')

if x == 3:
	x = input('Doğru Sayısı: ')

	y = input('Yanlış Sayısı: ')

	print('\n' * 50)

	z = (float(x) - (float(y)/4))

	print('Net: ' + str(z) + '\n' * 2) 
	input('\n\nÇıkmak için enter tuşuna bas.')  	