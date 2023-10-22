input("Enter length of the message you want to encrypt:");
disp(keygenerator(l));
function [key] = keygenerator(l)
%   This function generates a random key.
%   The key is of length suitable for the length of the message being encrypted in ACDFGVX.
%   This key should be kept secret and only be known to the attacker
keyl=floor(sqrt(l*2));
key=randsample(65:90,keyl);
end