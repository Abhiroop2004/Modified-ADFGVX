l=input("Enter length of the message you want to encrypt:");
disp(keygen(l));
function [key] = keygen(l)
%   This function generates a random key.
%   The key is of length suitable for the length of the message being encrypted in ACDFGVX.
%   This key should be kept secret and only be known to the attacker
keyl=ceil(sqrt(l));
key=randsample(65:90,keyl);
end
