% Sample User Interface for encrypting and decrypting text using the ACDFGVX Cipher
disp("Welcome to ACDFGVX encryting system:");
disp("You have the following choices:")
disp("1. To encrypt plain text(message)");
disp("2. To decrypt cipher text(encrypted data)");
c=input("Enter your choice:");
final=ACDFGVX(c);
if (c==1)
    fprintf("Cipher Text: \n%s",final);
elseif (c==2)
    fprintf("Plain Text: \n%s",final);
end
