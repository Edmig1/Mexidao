#include <iostream>
using namespace std;

main(){
	setlocale(LC_ALL, "Portuguese");
	
	 string mod,bag
	 ;
	
	int pes, por;
	
	float g, a, com;
	
	cout << "Escolha a marca do seu ve�culo";
	cin  >> mod;
	
	if(mod=="bmw"){
		cout << "okay, voc� tem uma BMW certo? ";
		g=9.8;
		a=8.9;
	}
	else if(mod=="fiat"){
		cout << "okay, voc� tem um Fiat certo? ";
		g=26.8;
		a=24.9;
	} else if(mod=="ferrari"){
		cout << "okay, voc� tem uma Ferrari certo? ";
		g=13.8;
		a=12.9;
	}
	else if(mod=="audi"){
		cout << "okay, voc� tem um Audi certo? ";
		g=12.8;
		a=10.9;
	}
	
	
	cout << "Quantas pessoas andam no carro?";
	cin >> pes;
	
	if(pes>2){
		g = g-1.2;
		a = a-1.2;
		
		
	}
	
	cout << "quantas portas o ve�culo possui?";
	cin >> por;
	
	if(por>4){
		g = g-0.5;
		a = a-0.5;
		
	}
	cout << "vai levar bagageiro na viagem?";
	cin >> bag;
	
	if(bag == "sim"){
		g= g-0.2;
		a= a-0.2;
	}
	cout << "Qual combust�vel o ve�culo usa?, responda com a para alcool, e g para gasolina";
	cin >> com;	
	
	if(com = g){
		cout << " seu carro iria utilzar " << g<<"Km/L na gasolina e";
	}
	if(com = a){
		cout << " seu carro iria utilzar " << a<<"Km/L no �lcool";
	}
	
	
	
}
