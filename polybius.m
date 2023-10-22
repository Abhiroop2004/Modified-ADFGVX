function [mapf] = polybius()
%  This function generates a 7x7 polybius square
%  The square contains 49 unique characters as follows: 
%   A-Z | 0-9 | space | symbols  ,.,''-_%+*@?() 
%   Def: A Polybius Square is a table that allows someone to convert letters into numbers.
%   The device is used for fractionating plaintext characters so that they can be represented by a smaller set of symbols, which is useful for telegraphy, steganography, and cryptography. 
%   According to Polybius' Histories, the device was invented by Cleoxenus and Democleitus, and further developed by Polybius himself.
%   The original square used the 24 Greek alphabets and space. (5x5)
map='';
map_alpha=char(randperm(26,26)+64);
for i=1:length(map_alpha)
    t=double(map_alpha(i))-64;
    map=append(map,map_alpha(i));
    if (t>0 && t<10)
        map=append(map,num2str(t));
    elseif (t==10)
        map=append(map,'0');
    end
end
mapsym=' .,''-_%+*@?()';
mapf='';
j=1;
order=randperm(26,13);
ordersym=randperm(13);
mapsym_r(ordersym)=mapsym;
for i=1:length(map)
    t=map(i);
    mapf=append(mapf,t);
    if (ismember(i,order))
        mapf=append(mapf,mapsym_r(j));
        j=j+1;
    end
end
writematrix(mapf,'polybius.txt');
