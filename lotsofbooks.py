from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, CategoryItem, User

# Create database and create a shortcut for easier to update database
engine = create_engine('sqlite:///catalogs.db',connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create first user
User1 = User(name="Zhas", email="test@gmail.com")
session.add(User1)
session.commit()

# Create category of Biography category
category1 = Categories(user_id=1, name="Biography")
session.add(category1)
session.commit()

# Create category of Business category
category2 = Categories(user_id=1, name="Business")
session.add(category2)
session.commit()

# Create category of Classics category
category3 = Categories(user_id=1, name="Classics")
session.add(category3)
session.commit()

# Create category of Fiction category
category4 = Categories(user_id=1, name="Fiction")
session.add(category4)
session.commit()

# Create category of Fantasy category
category5 = Categories(user_id=1, name="Fantasy")
session.add(category5)
session.commit()

# Create category of History category
category6 = Categories(user_id=1, name="History")
session.add(category6)
session.commit()

# Create category of Romance category
category7 = Categories(user_id=1, name="Romance")
session.add(category7)
session.commit()

# Create category of Science Fiction category
category8 = Categories(user_id=1, name="Science Fiction")
session.add(category8)
session.commit()

# Create category of Psychology category
category9 = Categories(user_id=1, name="Psychology")
session.add(category9)
session.commit()

# Create category of Horror category
category10 = Categories(user_id=1, name="Horror")
session.add(category10)
session.commit()



# Add Items into categories
categoryItem1= CategoryItem(user_id=1, 
                      name="The Diary of a Young Girl",
                      description="Anne Frank's extraordinary diary, \
                      written in the Amsterdam attic where she and her \
                      family hid from the Nazis for two years, has become \
                      a world classic and a timeless testament to the \
                      human spirit.",
                      categories=category1)

session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Rework",
                             description="Most business CategoryItem give \
                             you the same old advice: Write a business plan, \
                             study the competition, seek investors, yadda yadda. \
                             If you're looking for a book like that, put this one \
                             back on the shelf.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Alchemist",
                             description="Paulo Coelho's masterpiece tells \
                             the mystical story of Santiago, an Andalusian \
                             shepherd boy who yearns to travel in search of a \
                             worldly treasure. His quest will lead him to riches \
                             far different—and far more satisfying—than he ever \
                             imagined. Santiago's journey teaches us about the \
                             essential wisdom of listening to our hearts, of \
                             recognizing opportunity and learning to read the omens \
                             strewn along life's path, and, most importantly, to follow our dreams.",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="1984",
                             description="Among the seminal texts of the 20th century,\
                              Nineteen Eighty-Four is a rare work that grows more haunting \
                              as its futuristic purgatory becomes more real. Published in 1949, \
                              the book offers political satirist George Orwell's nightmare \
                              vision of a totalitarian, bureaucratic world and one poor stiff's \
                              attempt to find individuality. The brilliance of the novel is \
                              Orwell's prescience of modern life--the ubiquity of television, \
                              the distortion of the language--and his ability to construct such \
                              a thorough version of hell. Required reading for students since it \
                              was published, it ranks among the most terrifying novels ever written.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Fellowship of the Ring",
                             description="One Ring to rule them all, One Ring to find them, \
                             One Ring to bring them all and in the darkeness bind them \
                             In ancient times the Rings of Power were crafted by the \
                             Elven-smiths, and Sauron, The Dark Lord, forged the One Ring, \
                             filling it with his own power so that he could rule all others. \
                             But the One Ring was taken from him, and though he sought it throughout \
                             Middle-earth, it remained lost to him. After many ages it fell into the \
                             hands of Bilbo Baggins, as told in The Hobbit.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Sapiens: A Brief History of Humankind",
                             description="100,000 years ago, at least six human species \
                             inhabited the earth. Today there is just one. Us. Homo sapiens.\
                             How did our species succeed in the battle for dominance? \
                             Why did our foraging ancestors come together to create cities and kingdoms? \
                             How did we come to believe in gods, nations and human rights; to trust money, \
                             CategoryItem and laws; and to be enslaved by bureaucracy, timetables and consumerism? \
                             And what will our world be like in the millennia to come?",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Pride and Prejudice",
                             description="It is a truth universally acknowledged, \
                             that a single man in possession of a good fortune must be in want of a wife.\
                             Thus memorably begins Jane Austen's Pride and Prejudice, one of the world's \
                             most popular novels. Pride and Prejudice--Austen's own 'darling child'--tells the \
                             story of fiercely independent Elizabeth Bennett, one of five sisters who must marry rich, \
                             as she confounds the arrogant, wealthy Mr. Darcy. What ensues is one of the most \
                             delightful and engrossingly readable courtships known to literature, written by a \
                             precocious Austen when she was just twenty-one years old.",
                             categories=category7)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="World War Z",
                             description="The Zombie War came unthinkably close to eradicating humanity. \
                             Max Brooks, driven by the urgency of preserving the acid-etched first-hand \
                             experiences of the survivors from those apocalyptic years, traveled across the \
                             United States of America and throughout the world, from decimated cities that once \
                             teemed with upwards of thirty million souls to the most remote and inhospitable areas \
                             of the planet.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Power of Habit",
                             description="A young woman walks into a laboratory. \
                             Over the past two years, she has transformed almost \
                             every aspect of her life. She has quit smoking, run a marathon, \
                             and been promoted at work. The patterns inside her brain, \
                             neurologists discover, have fundamentally changed.",
                             categories=category9)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Salem's Lot",
                             description="Thousands of miles away from the small township of \
                             'Salem's Lot, two terrified people, a man and a boy, still share \
                             the secrets of those clapboard houses and tree-lined streets. \
                             They must return to 'Salem's Lot for a final confrontation with \
                             the unspeakable evil that lives on in the town.",
                             categories=category10)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="The Shining",
                             description="ack Torrance's new job at the Overlook Hotel \
                             is the perfect chance for a fresh start. As the off-season \
                             caretaker at the atmospheric old hotel, he'll have plenty of \
                             time to spend reconnecting with his family and working on his \
                             writing. But as the harsh winter weather sets in, the idyllic \
                             location feels ever more remote...and more sinister. And the \
                             only one to notice the strange and terrible forces gathering \
                             around the Overlook is Danny Torrance, a uniquely gifted five-year-old.",
                             categories=category10)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Smarter Faster Better",
                             description="WA new book that explores the science of productivity, \
                             and why, in today’s world, managing how you think—rather than what \
                             you think—can transform your life.",
                             categories=category9)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Foundation",
                             description="For twelve thousand years the Galactic Empire has ruled supreme. \
                             Now it is dying. But only Hari Seldon, creator of the revolutionary science of\
                              psychohistory, can see into the future -- to a dark age of ignorance, barbarism, \
                              and warfare that will last thirty thousand years. To preserve knowledge and save \
                              mankind, Seldon gathers the best minds in the Empire -- both scientists and scholars\
                               -- and brings them to a bleak planet at the edge of the Galaxy to serve as a\
                                beacon of hope for a future generations. He calls his sanctuary the Foundation.",
                             categories=category8)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="The Time Traveler's Wife",
                             description="A funny, often poignant tale of boy meets girl with a twist: \
                             what if one of them couldn't stop slipping in and out of time? Highly \
                             original and imaginative, this debut novel raises questions about life, \
                             love, and the effects of time on relationships.",
                             categories=category7)
session.add(categoryItem1)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="From Cold War to Hot Peace",
                             description="From one of America’s leading scholars of Russia who served as U.S.\
                              ambassador to Russia during the Obama administration, a revelatory, inside account \
                              of U.S.-Russia relations from 1989 to the presentIn 2008, when Michael McFaul was \
                              asked to leave his perch at Stanford and join an unlikely presidential campaign, \
                              he had no idea that he would find himself at the beating heart of one of today’s \
                              most contentious and consequential international relationships. ",
                             categories=category6)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Harry Potter and Sorcerer's Stone",
                             description="Harry Potter's life is miserable. His parents are dead and he's \
                             stuck with his heartless relatives, who force him to live in a tiny closet \
                             under the stairs. But his fortune changes when he receives a letter that tells \
                             him the truth about himself: he's a wizard. A mysterious visitor rescues him from \
                             his relatives and takes him to his new home, Hogwarts School of Witchcraft and Wizardry.",
                             categories=category5)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Life of Pi",
                             description="Life of Pi is a fantasy adventure novel by Yann Martel published in 2001. \
                             The protagonist, Piscine Molitor 'Pi' Patel, a Tamil boy from Pondicherry, \
                             explores issues of spirituality and practicality from an early age. He survives \
                             227 days after a shipwreck while stranded on a boat in the Pacific Ocean with a \
                             Bengal tiger named Richard Parker.",
                             categories=category4)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Crime and Punishment",
                             description="Raskolnikov, an impoverished student living in the \
                             St. Petersburg of the tsars, is determined to overreach his humanity \
                             and assert his untrammeled individual will. When he commits an act of \
                             murder and theft, he sets into motion a story that, for its excruciating \
                             suspense, its atmospheric vividness, and its depth of characterization \
                             and vision is almost unequaled in the literatures of the world. \
                             The best known of Dostoevsky’s masterpieces, Crime and Punishment \
                             can bear any amount of rereading without losing a drop of its power \
                             over our imaginations.",
                             categories=category3)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Think and Grow Rich",
                             description="Think and Grow Rich has been called the \
                             'Granddaddy of All Motivational Literature.' \
                             It was the first book to boldly ask, 'What makes a winner?'\
                              The man who asked and listened for the answer, Napoleon Hill,\
                               is now counted in the top ranks of the world's winners himself. \
                               The most famous of all teachers of success spent \
                               'a fortune and the better part of a lifetime of effort' \
                               to produce the 'Law of Success' philosophy that forms the basis \
                               of his CategoryItem and that is so powerfully summarized in this one.",
                             categories=category2)
session.add(categoryItem1)
session.commit()

categoryItem1 = CategoryItem(user_id=1, name="Elon Musk: Tesla, SpaceX, and the Quest for Fantastic Future",
                             description="Elon Musk, the entrepreneur and innovator behind SpaceX, \
                             Tesla, and SolarCity, sold one of his internet companies, PayPal, \
                             for $1.5 billion. Ashlee Vance captures the full spectacle and arc\
                              of the genius's life and work, from his tumultuous upbringing in \
                              South Africa and flight to the United States to his dramatic \
                              technical innovations and entrepreneurial pursuits. \
                              Vance uses Musk's story to explore one of the pressing \
                              questions of our age: can the nation of inventors and \
                              creators who led the modern world for a century still compete \
                              in an age of fierce global competition? ",
                             categories=category1)
session.add(categoryItem1)
session.commit()



print ("added category items!")
