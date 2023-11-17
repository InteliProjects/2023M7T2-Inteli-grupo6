
### Backend (Desenvolvido com NestJS)

#### **Visão Geral**

Utilizando a robusta estrutura **NestJS**, nosso backend serve como a ponte vital entre a interface intuitiva do usuário e nosso repositório de dados armazenados no banco de dados Postgresql, posicionado na AWS RDS. Mais do que simplesmente um ponto de conexão, ele desempenha um papel crucial em efetuar operações de dados, armazenamento e gestão de uploads para a AWS S3.

#### **Banco de Dados e ORM**

No núcleo de nossas operações de banco de dados, está o **Prisma** — nosso ORM preferido. Ele não apenas facilita o mapeamento de objetos para nossas tabelas de banco de dados, mas também otimiza cada operação realizada, garantindo eficiência e desempenho. Com nossa base de dados alojada na AWS RDS, garantimos três pilares essenciais: alta disponibilidade para atender a demandas escaláveis, segurança intransigente para proteger informações vitais e escalabilidade flexível para se adaptar a cargas de trabalho crescentes.

#### **Autenticação e Segurança**

A segurança e autenticação de cada usuário é primordial para nós. Com a implementação do **Passport**, oferecemos uma abordagem modular e flexível para autenticar usuários. Além disso, com a integração do **JWT** (JSON Web Tokens), asseguramos que cada sessão do usuário seja não apenas autenticada, mas também gerenciada de forma segura, garantindo integridade e confiabilidade em cada interação com nossa API.

#### **Processo de Upload e ETL**

A capacidade de nosso backend vai além de simplesmente aceitar e armazenar arquivos. Quando os usuários fazem upload de seus dados, nós os armazenamos de forma segura na AWS S3. Posteriormente, scripts externos de alta performance realizam um processo detalhado de ETL (Extração, Transformação e Carga). Após a conclusão dessa análise, qualquer previsão relevante relacionada à integridade do sistema de bleed é identificada, e os scripts atualizam diligentemente o registro relevante no banco de dados, garantindo que os usuários recebam feedback em tempo real.

#### **Rotas e Endpoints**

Nossos endpoints são projetados para serem intuitivos e eficientes. Aqui está um breve resumo:

##### **Flight**

- **GET** `/api/flight`: Fornece uma visão abrangente de todos os voos registrados.
- **GET** `/api/flight/{id}`: Oferece informações detalhadas e específicas sobre um voo em particular, com base no ID fornecido.
- **POST** `/api/flight/create`: Permite a adição eficiente de novos registros de voo.

##### **Authentication**

- **POST** `/api/auth/signup`: Desenhado para novos usuários, simplificando o processo de registro.
- **POST** `/api/auth/login`: Garante que os usuários existentes tenham uma experiência de login suave e segura.

##### **Users**

- **GET** `/api/users/profile`: Proporciona aos usuários uma visão detalhada de seus perfis.
- **PATCH** `/api/users/edit`: Permite que os usuários atualizem e modifiquem suas informações conforme necessário.
