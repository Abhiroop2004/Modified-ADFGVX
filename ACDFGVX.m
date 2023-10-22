%   This is an encryption system using ACDFGVX ciper (A modifies version of ADFGVX, which is upgraded version of ADFGX)
%   The ADFGVX Cipher was used by the German Army during World War I as a field cipher. 
%   It was an extension of the earlier ADFGX Cipher which worked in a very similar way. 
%   It was invented by Colonel Fritz Nebel, and it combines an adapted Polybius Square with Columnar Transposition.
%   It uses a 7x7 polybius square instead of the 6x6 in the original (or 5x5 in case of ADFGX).
m='ACDFGVX';
mapping=table2array(combinations(m,m));
file=fopen("polybius.txt","r");
poly=fscanf(file,'%c',51);
poly=strrep(poly,'"','');
acdfgvx=strcat(mapping,poly');

disp("Welcome to ACDFGVX encryting system:");
disp("You have the following choices:")
disp("1. To encrypt plain text(message)");
disp("2. To decrypt cipher text(encrypted data)");
c=input("Enter your choice:");
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
        cipher_i=reshape(message_s,[keyl,(padl/keyl)])';
        cipher_j=selection_sort(key,cipher_i);
        disp(cipher_j);
    case 2
        print();

end



function cipher_j = selection_sort(array,array1)
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