#include <iostream>
using namespace std;

main(){
	setlocale(LC_ALL, "Portuguese");
	
	string a, s, r, t, pix, cc, q, e;
	float v;
	
	
	cout<< "qual o tamanho do ovo? trabalhamos com: pequeno, m�dio e grande";
	cin>> t;
	if(t== "pequeno"){
		v=7.80;
	}
	
	if(t== "M�dio"){
		v=12.90;
	}
	
	if(t== "Grande"){
		v=23.95;
	}
	
	cout<< "qual sabor voc� deseja? temos chocolate preto, chocolate branco e chocolate ao leite!";
	cin>> s;
	
	if(s=="chocolate preto"){
		v= v+9.67;
	}
	
		if(s=="chocolate branco"){
		v= v+4.50;
	}
	
		if(s=="chocolate ao leite"){
		v= v+9.32;
	}
	
	cout<< "Escolha seu recheio, temos chocolate branco e chocolate preto, voce pode pedir misto!";
	cin >> r;
	
	if(r== "chocolate preto"){
	v = v+4.83;
	}
	
	
	if(r== "chocolate branco"){
			v = v+2.25;
	if(r== "misto")
	v = v+2.415+1.125;
	}

	
	cout<< "Escolha seu adicional, usamos kitkat e MM, pode optar por ambos tamb�m!";
	cin>> a;
	
	if(a== "kitkat"){
		v= v+4.67;
	}
	
		if(a== "MM"){
		v= v+5.53;
	}
		if(a== "ambos"){
		v= v+4.67+5.53;
	}
	
	cout<< "O pedido sera entregue via delivery?";
	cin>> e;
	
	if(e=="sim"){
		v= v+5;
	}
	
	cout << "o pagamento ser� via pix?";
	cin>> pix;
	
	if(pix=="sim"){
		v= v/1.10;
	}else{
		cout<<"o pagamento ser� no cart�o de cr�dito?";
		cin>> cc;
		if(cc=="sim"){
			v= v+3.30;
		}
	}
	
	cout << "O valor do seu produto foi de "<<v<< " reais";
	
}



