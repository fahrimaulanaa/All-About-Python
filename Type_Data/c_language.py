#tipe data dari bahasa pemrograman C
from ctypes import c_double, c_int, c_char

#tipe data numerik
c_double(10.5) #float
c_int(10) #integer

#tipe data karakter
c_char('A') #char
c_char(b'Hello') #string

#print tipe data
print(c_double(10.5))
print(c_int(10))
print(c_char('A'))
print(c_char_p(b'Hello'))
