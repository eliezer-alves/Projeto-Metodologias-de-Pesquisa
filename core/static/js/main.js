function retira_espaco(s){
	s = s.toString();
	if(s[0]==' '){
		s = s.substring(1);
		return retira_espaco(s);
	}if(s[s.length-1]==' '){
		s = s.substring(0,s.length-1);
		return retira_espaco(s);
	}
	return s;
}
function converter_maiusculo(s){
    var letra=s;
        letra=letra.split("");
        var value="";
        for(i=0;i<letra.length;i++){
            if(letra[i-1]){
            if(letra[i-1]==" "&&((letra[i+2]!=" "&&letra[i+3]!=" ")&&(i+2<letra.length&&i+3<letra.length))){
                letra[i]=letra[i].replace(letra[i],letra[i].toUpperCase());}
            }
            else{letra[i]=letra[i].replace(letra[i],letra[i].toUpperCase());}
            value+=letra[i];
        }
    return value;
}
function verifica_caractere(s){
        // 193 Á
        // 195
        // 199 Ç
        // 225 á
        // 
        // 226 â
        // 227 ã
        // 231 ç
        // 233 é
        // 234 ê
        // 237 í
        // 243 ó
        // 244 ô
        // 245 õ
        // 250 ú

    s=s.split("");
    var j;
    var h = "";
    for(var i=0;i<s.length;i++){
        j = s[i].charCodeAt(0);
        if(!((j>=65&&j<=90)||(j>=97&&j<=122)||(j>=190&&j<=250)||j==32)){
            s[i]="";
            //return false;
        }
        h+=s[i];
    }
    return h;
}
function validar_nom(i){
    //var erro = document.getElementById(e);
    var c = document.getElementById(i);
    //var s = c.value;

    c.value=verifica_caractere(c.value);
    c.value=retira_espaco(c.value);
    c.value=converter_maiusculo(c.value);
    var err_num = false;
    var s = c.value;
    if(!verifica_caractere(s)){
        //erro.innerHTML = '*valor inválido!'
        c.style.backgroundColor=   "#F8E0E0";
    }if(c.value==null||c.value==""){    	
        c.style.backgroundColor=   "white";
    }
    else if(s.length <= 1){
        //erro.innerHTML = '*valor inválido!'
        c.style.backgroundColor=   "#F8E0E0";
    }else if(err_num){
        //erro.innerHTML = '*valor inválido!'
        c.style.backgroundColor=   "#F8E0E0";
    }else{
        c.style.backgroundColor=   "#CEE3F6";
        //erro.innerHTML = "";
    }
}
function validar_email(i){
	var c = document.getElementById(i);
	c.value = retira_espaco(c.value);
	email = c.value;
	er = /^[a-zA-Z0-9][a-zA-Z0-9\._-]+@([a-zA-Z0-9\._-]+\.)[a-zA-Z-0-9]{2,3}/;
	if( !er.exec(email) )
	{
		document.getElementById('email').style.backgroundColor =   "#F8E0E0";
		
	}if(er.exec(email)){
		document.getElementById('email').style.backgroundColor =   "#CEE3F6";
	}if(c.value==null||c.value==""){    	
        c.style.backgroundColor=   "white";
    }

	
}
function validar_ass(i){
	var c = document.getElementById(i);
    c.value=retira_espaco(c.value);
    if(c.value==null||c.value==""){    	
        c.style.backgroundColor=   "white";
    }else{
        c.style.backgroundColor=   "#CEE3F6";
        //erro.innerHTML = "";
    }
}
function validar_select(i){
    var c = document.getElementById(i);
    c.value=retira_espaco(c.value);
    if(c.value==null||c.value==""){     
        c.style.backgroundColor=   "white";
    }else{
        c.style.backgroundColor=   "#CEE3F6";
        //erro.innerHTML = "";
    }    
}