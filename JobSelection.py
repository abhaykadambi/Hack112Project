def career_finder_quiz():
    print("Welcome to the Career Finder Quiz!")
    print("Answer the following questions to find your ideal career path.")
    
    score = {"STEM": 0, "Creative": 0, "Social": 0, "Entrepreneurial": 0}
    
    # Question 1: Interests
    print("\n1. Which activity do you enjoy most?")
    print("A) Solving puzzles")
    print("B) Designing something creative")
    print("C) Helping others solve problems")
    print("D) Starting new projects")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["STEM"] += 1
    elif answer == "B":
        score["Creative"] += 1
    elif answer == "C":
        score["Social"] += 1
    elif answer == "D":
        score["Entrepreneurial"] += 1

    # Question 2: Skills
    print("\n2. What are you naturally good at?")
    print("A) Analyzing data")
    print("B) Communicating with others")
    print("C) Building or fixing things")
    print("D) Coming up with new ideas")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["STEM"] += 1
    elif answer == "B":
        score["Social"] += 1
    elif answer == "C":
        score["Creative"] += 1
    elif answer == "D":
        score["Entrepreneurial"] += 1

    # Question 3: Values
    print("\n3. What motivates you the most?")
    print("A) Financial security")
    print("B) Creativity and freedom")
    print("C) Helping others")
    print("D) Building something new")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["STEM"] += 1
    elif answer == "B":
        score["Creative"] += 1
    elif answer == "C":
        score["Social"] += 1
    elif answer == "D":
        score["Entrepreneurial"] += 1

    result = max(score, key=score.get)
    if result == 'STEM':
        stem_career_quiz()
    elif result == "Creative":
        creative_career_quiz()
    elif result == 'Social':
        social_career_quiz()
    else:
        entrepreneurial_career_quiz()

def stem_career_quiz():
    
    score = {"Engineering": 0, "Life Sciences": 0, "Doctor": 0, "Academia": 0}

    # Question 1: Interests
    print("\n1. Which activity do you enjoy the most?")
    print("A) Designing and building machines or systems")
    print("B) Researching living organisms and ecosystems")
    print("C) Helping patients and working in healthcare")
    print("D) Teaching or conducting research in a university")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Engineering"] += 1
    elif answer == "B":
        score["Life Sciences"] += 1
    elif answer == "C":
        score["Doctor"] += 1
    elif answer == "D":
        score["Academia"] += 1

    # Question 2: Work Environment
    print("\n2. Where do you see yourself working?")
    print("A) In a company or field site building solutions")
    print("B) In a lab researching biological processes")
    print("C) In a hospital or clinic treating patients")
    print("D) In a university conducting research and teaching")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Engineering"] += 1
    elif answer == "B":
        score["Life Sciences"] += 1
    elif answer == "C":
        score["Doctor"] += 1
    elif answer == "D":
        score["Academia"] += 1

    # Question 3: Skills
    print("\n3. What is your strongest skill?")
    print("A) Problem-solving and designing systems")
    print("B) Understanding biological processes")
    print("C) Diagnosing and treating patients")
    print("D) Writing papers and teaching concepts")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Engineering"] += 1
    elif answer == "B":
        score["Life Sciences"] += 1
    elif answer == "C":
        score["Doctor"] += 1
    elif answer == "D":
        score["Academia"] += 1

    # Question 4: Career Goals
    print("\n4. What is your ultimate career goal?")
    print("A) Innovating practical solutions to real-world problems")
    print("B) Advancing our understanding of living systems")
    print("C) Improving the health and lives of others")
    print("D) Becoming a thought leader in a specific field")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Engineering"] += 1
    elif answer == "B":
        score["Life Sciences"] += 1
    elif answer == "C":
        score["Doctor"] += 1
    elif answer == "D":
        score["Academia"] += 1

    # Results
    print("\nCalculating your ideal STEM career path...")
    result = max(score, key=score.get)
    print(f"\nBased on your answers, your ideal STEM career might be in: {result}!")

def creative_career_quiz():
    
    # Initialize score for simplified creative fields
    score = {"Design": 0, "Writing": 0, "Music": 0, "Marketing": 0}

    # Question 1: Type of Creativity
    print("\n1. Which type of creativity excites you the most?")
    print("A) Designing digital art or products")
    print("B) Writing articles, stories, or scripts")
    print("C) Composing music or soundscapes")
    print("D) Creating marketing strategies or campaigns")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Design"] += 1
    elif answer == "B":
        score["Writing"] += 1
    elif answer == "C":
        score["Music"] += 1
    elif answer == "D":
        score["Marketing"] += 1

    # Question 2: Skills & Strengths
    print("\n2. Which skill do you think you're most skilled at?")
    print("A) Visual design, illustration, or layout")
    print("B) Writing engaging, creative, and original content")
    print("C) Understanding musical theory and creating melodies")
    print("D) Developing strategies for product or brand promotion")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Design"] += 1
    elif answer == "B":
        score["Writing"] += 1
    elif answer == "C":
        score["Music"] += 1
    elif answer == "D":
        score["Marketing"] += 1

    # Question 3: Work Environment Preference
    print("\n3. Where do you see yourself working?")
    print("A) In a creative studio or working on digital design projects")
    print("B) Writing for a blog, magazine, or publishing house")
    print("C) In a studio creating music or soundtracks")
    print("D) In a marketing agency or as a brand strategist")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Design"] += 1
    elif answer == "B":
        score["Writing"] += 1
    elif answer == "C":
        score["Music"] += 1
    elif answer == "D":
        score["Marketing"] += 1

    # Question 4: Desired Impact of Your Work
    print("\n4. What impact do you want your work to have?")
    print("A) Transform how people interact with design and technology")
    print("B) Move people with powerful, thoughtful storytelling")
    print("C) Create experiences and emotions through music and sound")
    print("D) Influence consumer behavior and build brand loyalty")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Design"] += 1
    elif answer == "B":
        score["Writing"] += 1
    elif answer == "C":
        score["Music"] += 1
    elif answer == "D":
        score["Marketing"] += 1

    # Results
    print("\nCalculating your ideal creative career path...")
    result = max(score, key=score.get)
    print(f"\nBased on your answers, your ideal creative career might be in: {result}!")

def social_career_quiz():
    
    # Initialize score for different social fields
    score = {"Counseling": 0, "Education": 0, "Public Relations": 0, "Nonprofit Work": 0}

    # Question 1: Motivations
    print("\n1. What motivates you most?")
    print("A) Helping others improve their mental health")
    print("B) Teaching or mentoring others")
    print("C) Building relationships and creating positive public images")
    print("D) Making a meaningful impact on communities or causes")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Counseling"] += 1
    elif answer == "B":
        score["Education"] += 1
    elif answer == "C":
        score["Public Relations"] += 1
    elif answer == "D":
        score["Nonprofit Work"] += 1

    # Question 2: Communication Style
    print("\n2. How do you prefer to communicate with others?")
    print("A) One-on-one conversations to listen and offer support")
    print("B) Giving presentations or teaching in front of a group")
    print("C) Creating press releases, managing media, and public events")
    print("D) Organizing community events and working with diverse groups")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Counseling"] += 1
    elif answer == "B":
        score["Education"] += 1
    elif answer == "C":
        score["Public Relations"] += 1
    elif answer == "D":
        score["Nonprofit Work"] += 1

    # Question 3: Working Environment
    print("\n3. What type of environment do you thrive in?")
    print("A) A clinical or therapy setting, providing one-on-one counseling")
    print("B) A classroom, teaching or mentoring students of all ages")
    print("C) A fast-paced media or public relations agency, interacting with clients")
    print("D) A nonprofit organization or community center working on social causes")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Counseling"] += 1
    elif answer == "B":
        score["Education"] += 1
    elif answer == "C":
        score["Public Relations"] += 1
    elif answer == "D":
        score["Nonprofit Work"] += 1

    # Question 4: Skills & Strengths
    print("\n4. Which skill do you think you're most skilled at?")
    print("A) Empathy, active listening, and problem-solving")
    print("B) Explaining complex concepts clearly and inspiring others")
    print("C) Writing compelling messages, handling crises, and public speaking")
    print("D) Organizing events, fundraising, and advocating for causes")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Counseling"] += 1
    elif answer == "B":
        score["Education"] += 1
    elif answer == "C":
        score["Public Relations"] += 1
    elif answer == "D":
        score["Nonprofit Work"] += 1

    # Question 5: Challenges You Enjoy
    print("\n5. Which type of challenge excites you most?")
    print("A) Helping people overcome emotional or mental obstacles")
    print("B) Helping students achieve success and personal growth")
    print("C) Managing a public image and building a positive reputation")
    print("D) Advocating for social causes and making an impact on communities")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Counseling"] += 1
    elif answer == "B":
        score["Education"] += 1
    elif answer == "C":
        score["Public Relations"] += 1
    elif answer == "D":
        score["Nonprofit Work"] += 1

    # Question 6: Desired Impact
    print("\n6. What impact do you want your work to have?")
    print("A) Helping individuals improve their mental well-being")
    print("B) Educating others and empowering students with knowledge")
    print("C) Shaping public perception and managing brand reputation")
    print("D) Creating lasting social change and community support")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Counseling"] += 1
    elif answer == "B":
        score["Education"] += 1
    elif answer == "C":
        score["Public Relations"] += 1
    elif answer == "D":
        score["Nonprofit Work"] += 1

    # Results
    print("\nCalculating your ideal social career path...")
    result = max(score, key=score.get)
    print(f"\nBased on your answers, your ideal social career might be in: {result}!")

def entrepreneurial_career_quiz():
    
    score = {"Startup Founder": 0, "Venture Capitalist": 0, "Freelancer": 0, "Business Manager": 0}

    # Question 1: Approach to Work
    print("\n1. How do you prefer to approach work?")
    print("A) Building and launching new ideas")
    print("B) Investing in innovative businesses")
    print("C) Working independently with clients")
    print("D) Managing teams and projects")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Question 2: Risk Tolerance
    print("\n2. How do you handle risk?")
    print("A) I embrace risk as an essential part of creating something new")
    print("B) I prefer to analyze risk and invest where I see potential growth")
    print("C) I like low risk but enjoy the challenge of delivering high-quality work")
    print("D) I manage risk carefully by ensuring processes and teams are efficient")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Question 3: Work Environment Preference
    print("\n3. What type of work environment do you thrive in?")
    print("A) A fast-paced, high-pressure environment where I create new products")
    print("B) A strategic and financial environment, analyzing and evaluating opportunities")
    print("C) A flexible, independent environment with autonomy in my work")
    print("D) A structured environment where I can lead and manage teams effectively")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Question 4: Passion & Motivation
    print("\n4. What motivates you to succeed?")
    print("A) The thrill of creating something from nothing and solving new problems")
    print("B) Identifying and backing the next big business opportunity")
    print("C) Helping clients achieve their goals while maintaining flexibility")
    print("D) Leading a team to execute plans and achieve company goals")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Question 5: Working with Others
    print("\n5. How do you prefer to work with others?")
    print("A) Collaborating with a small team to innovate and build products")
    print("B) Working with entrepreneurs to find and nurture promising startups")
    print("C) Building strong relationships with clients to understand their needs")
    print("D) Leading teams and ensuring everyone is working towards a shared vision")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Question 6: Long-Term Vision
    print("\n6. What is your long-term vision for your career?")
    print("A) Growing my own company and possibly leading it to become a major player in the market")
    print("B) Building a portfolio of successful investments and supporting innovation")
    print("C) Establishing a strong personal brand and consistently attracting clients")
    print("D) Leading a well-established business and scaling operations for long-term growth")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Question 7: Financial Perspective
    print("\n7. How do you approach finances?")
    print("A) I prefer to invest my own money into projects I believe in")
    print("B) I enjoy evaluating financial opportunities and risk for investment")
    print("C) I keep my financials simple, focusing on clients and manageable projects")
    print("D) I work on maximizing profit through cost optimization and team efficiency")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Question 8: Handling Stress
    print("\n8. How do you handle stress and pressure?")
    print("A) I thrive under pressure, turning challenges into opportunities for growth")
    print("B) I stay calm and focus on evaluating the situation from a strategic angle")
    print("C) I prioritize my work and stay organized to meet client demands and deadlines")
    print("D) I remain composed, ensuring my team stays on track to meet targets")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == "A":
        score["Startup Founder"] += 1
    elif answer == "B":
        score["Venture Capitalist"] += 1
    elif answer == "C":
        score["Freelancer"] += 1
    elif answer == "D":
        score["Business Manager"] += 1

    # Results
    print("\nCalculating your ideal entrepreneurial career path...")
    result = max(score, key=score.get)
    print(f"\nBased on your answers, your ideal entrepreneurial career might be as a: {result}!")

career_finder_quiz()