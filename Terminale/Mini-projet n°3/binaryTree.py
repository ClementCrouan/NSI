class BinaryTree :
    def __init__(self, rep, q = None, left = None, right = None, res = None):
        self.reponse = rep
        self.question = q 
        self.left = left
        self.right = right
        self.result = res

    def change_left(self, left):
        self.left = left
    def change_right(self, right):
        self.right = right

    def parcours_infixe(self, n = 0):
        if self.left is not None:
            self.left.parcours_infixe(n+2)
        print(n*' ', '->', self.question)
        if self.right is not None:
            self.right.parcours_infixe(n+2)
    def __str__(self) -> str:
        return f'{self.value}({self.left}, {self.right})'
    
def character_chimie():
    tree = BinaryTree(None, "Vous commencez vos études ! Vous avez choisi les majeures Maths et Chimie. Malheureusement, demain, examen de chimie. Que faites vous ?",
        BinaryTree("Aller voir Medhi","Medhi vous propose un buisness un peu douteux. Que faire ?",
            BinaryTree("Vous retournez réviser votre chimie","Medhi ne veux pas vous laisser partir avec son secret. Dommage. Perdu !", None, None, False),
            BinaryTree("Devenir dealer","Vous échouez votre examen de chimie mais medhi sait apprécier vos compétences en chimie (rapport à la drogue). Pour prendre de l'importance dans la bande à Medhi (et vendre plus de drogue),", 
                BinaryTree("Vous contactez le nerd pour faire un site Internet", "Le nerd a vu 'how to sell drugs online', il est donc hypé.",
                    BinaryTree("Vous le tuez et lui volez son site", "Le nerd a un iPhone 14, qui appelle automatiquement les urgences en cas de problème. Mourrir en est un. Perdu !", None, None, False),
                    BinaryTree("Vous lui donnez beaucoup de crypto moulaga pour gagner sa confiance", "Motivé, il vous donne un super site et annonce même connaitre le commercial.", 
                        BinaryTree("Vous tuez le commercial et volez son entrepot", "Arrête de vouloir tuer tout le monde c'est une dinguerie (tu fais ca parce qu'il est noir ???). Perdu !", None, None, False),
                        BinaryTree("Vous donnez beaucoup de carte cadeau amazon au commercial pour gagner sa confiance", "Motivé, il vous donne un super entrepot et vous donne même le numéro du chomeur (client potentiel !).", None, None, True))),
                BinaryTree("Vous contactez le commercial pour obtenir un entrepot", "ratio cléante", None, None, True))),
        BinaryTree("Réviser votre chimie", "Vous excellez en chimie et majorez votre classe.", 
            BinaryTree("Profitez de vos notes pour intégrer le MIT", "Vous recevez un prix nobel de chimie et êtes professeur. Vous êtes malheureusement atteint du cancer, et décidez de vivre vos dernières années dans la drogue.",
                BinaryTree("Au Mexique, avec el chapo", "El chapo, très ambitieux et effrayé de votre talent, décide d'éliminer la concurrence. Perdu !", None, None, False),
                BinaryTree("En Colombie, avec Pablo Escobar", "Vous prospérez une dizaine d'année dans la drogue et devenez plus puissant que Escobar, mais votre cancer vous rattrape. Perdu !", None, None, False)),
            BinaryTree("Profitez de vos compétences pour intégrer des cartels", "Devant la qualitée de votre meth (meilleure que celle de Medhi), Escobar vous propose de diriger votre propre division",
                BinaryTree("Au Mexique, avec el chapo", "Lisez les infos. El chapo est tombé, et vous aussi. Perdu !", None, None, False),
                BinaryTree("En Colombie, avec Pablo Escobar", "Votre ancien professeur n'est pas d'accord avec votre redirection. Interpole non plus. Perdu !", None, None, False))))
    return tree

def character_nerd():
    tree = BinaryTree(None, "Vous commencez vos études ! Vous avez choisi les majeures Maths et Informatique. Malheureusement, demain, examen pratique de html. Que faites vous ?",
        BinaryTree("Aller sur l'internet sombre","L'utilisateur 'MedhiGOAT' vous propose un buisness un peu douteux. Que faire ?",
            BinaryTree("Vous retournez réviser votre html","MedhiGOAT ne veux pas vous laisser partir avec son secret, il vous menace !",
                BinaryTree("Vous le frappez violemment pour qu'il aille se rendormir","Mehdi refuse de dormir...",
                    BinaryTree("Vous lui proposez des somnifères","Il les accepte et retourne dormir dans son pays", None, None, True),
                    BinaryTree("Vous dormez","Vous rêvez de MedhiGOAT. Quelle charisme, vous voudriez l'épouser.", None, None, False)),
                BinaryTree("Vous lui offrez tout votre argent et devenez son esclave","MehdiGOAT vous demande en mariage !",
                    BinaryTree("Vous acceptez","Vous vous mariez mais MehdiGOAT vous force à devenir vendeur de drogue... :(",
                        BinaryTree("Oui reine Fatima", "Ils vécurent riche eurent beaucoup d'enfants (dealers eux aussi). Fin !", None, None, True),
                        BinaryTree("Vous vous opposez à cette ordre car il vous reste un peu d'amour propre", "Il vous frappe à mort. (pas cool)", None, None, False)),
                    BinaryTree("Vous refusez (no homo)","Il tombe amoureux de votre frère et décide de vous laisser tranquille.", None, None, True))),
            BinaryTree("Devenir e-dealer","Votre professeur, impressioné par votre site d'e-drogue, vous met 20 et vous êtes premier de votre classe.",
                BinaryTree("Revenir dans la voie de la lumière (s/o le maitre de l'air)", "Le studio du maitre de l'air accepte de vous embaucher !", 
                    BinaryTree("Vous promulguez votre propre documentaire sur les capybaras", "Avec l'aide du commercial vous pour la pub, vous réalisez un chef d'oeuvre vraiment émouvant. Bravo !", None, None, True),
                    BinaryTree("Vous produisez un film francais d'action","Vous floppez et Arkunir décide de vous ratio (ratio).", None, None, False)),
                BinaryTree("Ratio Escobar", "Vous floppez mais un capybara viens vous aider.", 
                    BinaryTree("Pour le remercier, vous essayez de sauver son frère détenu par Medhi", "Son frère vous ratio et vous êtes ban twitter !", None, None, False), 
                    BinaryTree("Vous chantez 'OK I PULL UP'","Capybara utilise technique du serpent secret !", None, None, True)))),
        BinaryTree("Réviser votre html", "Votre professeur est impressionné par votre site de revente de matériel gaming.", 
            BinaryTree("Modifier votre site pour concurencer Amazon", "L'utilisateur 'MedhiGOAT' est interessé par votre site, mais pas pour vendre des bonbons.",
                BinaryTree("Refuser poliment (les hendeks ca fait peur)", "MedhiGOAT déteste se faire recaller ... :(",
                    BinaryTree("Pour le calmer, vous lui offrez un casque gaming", "Réconciliés, MedhiGOAT vous propose de duo queue sur LOL !", 
                        BinaryTree("Vous refusez, par crainte pour votre élo", "Vous finissez immortal en solo queue, gg !", None, None, True),
                        BinaryTree("Vous ne jouez pas à Valorant, vous préférez vous doucher", "Un nerd ne se douche jamais. Vous mourrez dans d'atroces souffrances.", None, None, False)),
                    BinaryTree("Pleure", "Jugé 'cancer' par MedhiGOAT, il vous signale. Vous êtes ban 563463465 heures.", None, None, False)),
                BinaryTree("Argent argent argent argent", "Vous demandez une somme tantôt élevée à MedhiGOAT, qui décide de vous faire chanter (comment il a eu cette vidéo ???). ",                 
                    BinaryTree("Appeler la police", "Vous ne vous souvenez plus du numéro de la police !!!!", 
                        BinaryTree("Vous regardez sur Internet", "Vous tombez sur le mauvais site et perdez vos coordonnées bancaires",  
                            BinaryTree("Vous déclenchez un combat de hackers", "Vous faites du html, pas de la cybersécurité...", None, None, False),
                            BinaryTree("Vous leur laissez tout votre argent et pleurez à chaudes larmes", "Emus, ils décident de vous laisser partir si vous répondez à cette question de quipoquiz :\nEn 1970, l’auteur de science-fiction Arthur C. Clarke avait prédit avec précision ce que deviendrait l’Internet.", 
                                BinaryTree("Vrai", "Bonne réponse !", None, None, True), 
                                BinaryTree("Faux", "Vous avez aussi peu de culture que McFly et Carlito.", None, None, False))), 
                        BinaryTree("Vous demandez à votre mère", "Maman a toujours réponse à tout.", None, None, True)),
                    BinaryTree("Le menacer en retour", "Tu déclenche une guerre de gang, alors que tu n'as pas de gang. Perdu !", None, None, False)),),
            BinaryTree("J'ai pas d'idée, imaginez un truc cool", "Le manque d'idée ne vous mènera pas loin...",
                BinaryTree("Se reprendre en main", "Bonne décision. Les bonnes décisions rendent riche.", None, None, True),
                BinaryTree("Perdu pour perdu, allons voir MedhiGOAT", "Vous avez mérité de rater votre vie.", None, None, False))))
    return tree

def character_commercial():
    tree = BinaryTree(None, "Vous commencez vos études ! Vous avez choisi les majeures Maths et SES. Malheureusement, demain, examen d'économie. Que faites vous ?",
        BinaryTree("Aller sur Amazon","L'utilisateur 'Medhi->tarifsEnBio' vous propose d'étudier la pratique.",
            BinaryTree("Utiliser vos talents de commercial pour vendre un max de meth","En plus d'échouer votre examen d'économie, les modos amazon (oui ils existent) appellent la police. Qui vend de la drogue sur amazon aussi ???", None, None, False),
            BinaryTree("La drogue c'est pas bien, dis le à tes copains","Vous réussissez à convaincre Medhi->tarifsEnBio d'arrêter la drogue (car c'est mal). Vous lui conseillez : ", 
                BinaryTree("D'aller se repentir au près du Père Papa", "Grosse erreur, Medhi->tarifsEnBio est musulman !", None, None, False), 
                BinaryTree("D'aller se faire foutre", "Grosse révélation pour Medhi->tarifsEnBio, il est gay ! Il vous remercie de lui avoir ouvert les yeux.", None, None, True))),
        BinaryTree("Réviser votre économie", "Vous excellez à l'examen, et votre professeur voit un grand talent en vous.", 
            BinaryTree("Partez travailler chez amazon", "Vous dirigez un entrepot amazon et êtes réputé dans le monde entier. Le chimiste demande de privatiser un entrepot.", 
                BinaryTree("Argent argent argent (un peu de drogue aussi)", "Le chimiste se trouve être un énorme rat.",
                    BinaryTree("Vous êtes un mâle alpha et le rackettez", "Effrayé, il fuit et vous finissez pauvre...", 
                        BinaryTree("La cigale ayant chantée tout l'été, vous suppliez le nerd de vous aider", "Il accepte de vous aider en échange d'un capybara.",
                            BinaryTree("OK I PULL UP", "Quel chad, vous méritez cette victoire.", None, None, True),
                            BinaryTree("Vous lui dites de désinstaller TikTok", "Ratio", None, None, False)),
                        BinaryTree("Vous partez vivre sous un pont", "David, le sdf du coin vous lance un duel pour conquérir le pont.",
                            BinaryTree("Effrayé part son charisme, vous sautez du pont", "Pire facon de perdre. Sale newbienoob.", None, None, False),
                            BinaryTree("Technique du serpent secret", "Je sais pas ce que vous avez fait, mais ca a marché.", None, None, True))),
                    BinaryTree("Vous vous soumettez et imposez sa clémence", "Il vous demande un milkshake au chocolat :", 
                        BinaryTree("Vous vous trompez et lui donnez un caffe latté", "Deuxième erreur, vous confondez caffé latté et canard laqué... C'en est trop pour le chimiste.", None, None, False),
                        BinaryTree("Vrai sujet on est en 2023 y a encore des gens qui prennent des milkshakes ?", "Je vous offre cette victoire, pour lutter contre les milkshakes.", None, None, True))),
                BinaryTree("Arrière gueux, ou j'appelle la police !", "Medhi->tarifsEnBio souhaite vous empaler, avec la musique du poto JUL en fond. Ca doit être horrible.", 
                    BinaryTree("Vous avez fait un an de judo en primaire", "Medhi->tarifsEnBio a fait 2 ans de judo en primaire... ", None, None, False),
                    BinaryTree("Vous utilisez vos chaussures qui courent vite", "Vous gagnez la course jusqu'au comissariat, et battez le précédent record d'Usain Bolt !", None, None, True))),
            BinaryTree("A chier le capitalisme, vous decidez de vivre au jour le jour","Comment ca mon boeuf ? Sale pauvre.", None, None, False)))
    return tree
                        