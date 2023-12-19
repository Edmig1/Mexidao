t = (input("qual o tamanho do ovo? trabalhamos com: pequeno, médio e grande: "))
s = (input("qual sabor você deseja? temos chocolate preto, chocolate branco e chocolate ao leite: "))
r = (input("Escolha seu recheio, temos chocolate branco e chocolate preto, voce pode pedir misto: "))
a = (input("Escolha seu adicional, usamos kitkat e MM, pode optar por ambos também: "))


v = 0.0

# Tamanho
if (t=="pequeno"):
    v = v + 7.80


elif (t=="médio"):
    v = v + 12.90

elif (t=="grande"):
    v = v + 23.95
# Sabor

if(s=="chocolate preto"):
    v = v + 9.67

if(s=="chocolate branco"):
    v = v + 4.50

if(s=="chocolate ao leite"):
    v = v + 9.32

# Recheio
if(r=="chocolate preto"):
	v = v+4.83
        
if(r=="chocolate branco"):
	v = v+2.25

if(r=="misto"):
	v = v+2.415+1.125
        
# Adicionais

if(a== "kitkat"):
	v= v+ 4.67
	
	
if(a== "MM"):
	v= v+ 5.53
	
if(a== "ambos"):
	v= v + (4.67+ 5.53) / 2
        
print("O pedido será entregue via delivery?")
e = input()

if e == 'sim':
    v = v + 5

print("O pagamento será via PIX?")
pix = input()

if pix == 'sim':
    v = v / 1.10
else:
    print("O pagamento será no cartão de crédito?")
    cc = input()
    if cc == 'sim':
        v = v + 3.30

print(f"O valor do seu produto foi de {v:.2f} reais")

if t.lower() == "médio":
    v = v + 12.90


