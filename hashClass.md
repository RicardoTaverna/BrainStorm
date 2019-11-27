# Hash em Python

## O que é Hash
O Hashing refere-se ao processo de geração de uma saída (output) de tamanho fixo a partir de uma entrada (input) de tamanho variável. Isto é feito através do uso de fórmulas matemáticas conhecidas como funções hash (implementado como algoritmos de hashing). 

## Criptografia
Criptografia é o ato de codificar dados em informações aparentemente sem sentido, para que pessoas não consigam ter acesso às informações que foram cifradas. Há vários usos para a criptografia em nosso dia-a-dia: proteger documentos secretos, transmitir informações confidenciais pela Internet ou por uma rede local, etc.

Em geral, romper uma função hash criptográfica requer milhares de tentativas forçadas (brute-force attempts). Para uma pessoa “reverter” uma função hash criptográfica, seria necessário adivinhar qual foi o input através de tentativa e erro até conseguir finalmente gerar o output correspondente.

Quando combinados com criptografia, os algoritmos de hashing podem ser muito versáteis, oferecendo segurança e autenticação de muitas maneiras diferentes.

## Funções Hash

### SHA
O acrônimo SHA significa Secure Hash Algorithms (Algoritmos de Hash Seguros). 
Refere-se a um conjunto de funções hash criptográficas que incluem os algoritmos SHA-0 e SHA-1 em conjunto com os grupos SHA-2 e SHA-3. 
O SHA-256 faz parte do grupo SHA-2, juntamente com o SHA-512 e outras variantes.

### MD5
O MD5 (Message-Digest algorithm 5) é um algoritmo de hash de 128 bits unidirecional desenvolvido pela RSA Data Security, Inc.
Por ser um algoritmo unidirecional, um hash MD5 não pode ser transformado novamente na password (ou texto) que lhe deu origem. O método de verificação é, então, feito pela comparação das duas hash (uma da base de dados, e a outra da tentativa de login).
O MD5 é de domínio público para uso em geral. A partir de uma mensagem de um tamanho qualquer, ele gera um valor hash de 128 bits; com este algoritmo, é computacionalmente impraticável descobrir duas mensagens que gerem o mesmo valor, bem como reproduzir uma mensagem a partir do seu digest. O algoritmo MD5 é utilizado como mecanismo de integridade em vários protocolos de padrão Internet (RFC1352, RFC1446, etc.), bem como pelo CERT e CIAC.

Message Digests são funções hash que geram código de tamanho fixo, em uma única direção, a partir de dados de tamanho arbitrário. Esses códigos hash são extremamente úteis para segurança de senhas. Como ele não pode ser descriptografado, o código hash precisa ser re-gerado e comparado com a seqüência disponível anteriormente. Se ambos se igualarem, o acesso é liberado.
