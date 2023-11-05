%   The ADFGVX Cipher was used by the German Army during World War I as a field cipher. 
%   It was an extension of the earlier ADFGX Cipher which worked in a very similar way. 
%   It was invented by Colonel Fritz Nebel, and it combines an adapted Polybius Square with Columnar Transposition.
%   It uses a 7x7 polybius square instead of the 6x6 in the original (or 5x5 in case of ADFGX).
%   Source: Wikipedia, CRYPTO CORNER.
function [final] = ACDFGVX(c)
m='ACDFGVX';
mapping=table2array(combinations(m,m));
file=fopen("polybius.txt","r");
poly=fscanf(file,'%c',51);
poly=strrep(poly,'"','');
acdfgvx=strcat(mapping,poly');
switch c
    case 1
        %This is the code for encrypting data
        c=input("Enter text to encrypt:",'s');
        key=input("Enter your secret key unique to the sender:",'s');
        c=upper(c);
        message_s='';
        l=length(c);
        for i=1:l
            t=c(i);
            for j=1:49
                if acdfgvx(j,3)==t
            message_s=append(message_s,acdfgvx(j,1:2));
                end
            end
        end
        keyl=length(key);
        padl=ceil((l*2)/keyl)*keyl;
        message_s=pad(message_s,padl);
        disp(message_s);
        row_n=padl/keyl;
        % Columnar Transposition
        cipher_i=reshape(message_s,[keyl,row_n])';
        cipher_j=selection_sort(key,cipher_i,keyl);
        final=reshape(cipher_j,[1,padl]);
        
        % Row Transposition
        %t=cipher_j(i,:);
        %cipher_j()   

    case 2
        c=input("Enter text to decrypt:",'s');
        key=input("Enter your secret key unique to the sender:",'s');
        l=length(c);
        keyl=length(key);
        padl=ceil((l)/keyl)*keyl;
        c=reshape(c,[padl/keyl, keyl]);
        pt=selection_sort(key,c,keyl);
        final=reshape(pt,[1,padl]);
        % This portion hasn't been developed yet
end

function cipher_j = selection_sort(array,array1,keyl)
  len = length(array);
  for i=1:1:len
    min=i;
    for j=i+1:1:len
        if array(j)<array(min)
            min=j;
        end       
    end
    temp1=array1(:,i);
    array1(:,i)=array1(:,min);
    array1(:,min)=temp1;
    temp=array(:,i);
    array(:,i)=array(:,min);
    array(:,min)=temp;
  end
  cipher_j=char(array1);
end
end
