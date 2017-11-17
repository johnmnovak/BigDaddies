class Student:
    students = []
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.points = 0
        self.skills = []
        self.guilds = []
        self.pointsToNextLevel = self.level * self.level * 10
        Student.students.append(self)
        
    def __str__(self):
        return(self.name)
    
    def __repr__(self):
        return(self.name)
        
    def generateReport(self):
        return('*******************************\nStudent Name: {}\nLevel: {}\nPoints: {}/{}\nSkills: {}\nGuilds: {}\n*******************************\n'.format(self.name, self.level, self.points, self.pointsToNextLevel, self.skills, self.guilds))
    
    def addSkill(self, skillName):
        newSkill = Skill(skillName)
        self.skills.append(newSkill)
        
    def addToGuild(self, guild):
        self.guilds.append(guild)
        
    def addPoints(self, points, pointType):
        self.points += points
        self.checkLevelUp()
        
        for item in self.skills:
            if (item.name == pointType):
                item.points += points
                item.checkLevelUp()
        
    def checkLevelUp(self):
        if(self.pointsToNextLevel <= self.points):
            self.level += 1
            self.pointsToNextLevel = self.level * self.level * 10
        else:
            return
        self.checkLevelUp()
        
    def rankBySkill(skill):
        pass
        
        
        
##################
class Guild:
    def __init__(self, name, creator):
        self.name = name
        self.members = [creator]
        creator.addToGuild(self)
        
    def __str__(self):
        return(self.name)
    
    def __repr__(self):
        return(self.name)
        
    def generateReport(self):
        return('Guild Name: {}\nMembers: {}\nAverage Member Level: {}'.format(self.name, self.members, self.getAverageLevel()))
    
    def addMember(self, newMember):
        self.members.append(newMember)
        newMember.addToGuild(self)
        
    def getAverageLevel(self):
        total = 0
        for item in self.members:
            total += item.level
        return (total/len(self.members))
            
##################
class Skill:
    skillList = ['Math', 'Reading Comprehension', 'Geogrpahy', 'History', 'Being Sexy']
    def __init__(self, skillName):
        if(skillName in Skill.skillList):
            self.name = skillName
            self.level = 1
            self.points = 0
        else:
            return
        
    def __str__(self):
        return('{} ({})'.format(self.name, self.level))
    
    def __repr__(self):
        return('{} ({})'.format(self.name, self.level))
    
    def checkLevelUp(self):
        if (self.level * 10 <= self.points):
            self.level += 1
        else:
            return
        self.checkLevelUp()
##################

class Quest:
    pass

    
##################

class Quiz(Quest):
    pass

    
    
##################

def main():
    john = Student('John Novak')
    john.addSkill('Math')
    john.addSkill('History')
    john.addPoints(20, 'Math')
    g = Guild('Guild 1', john)
    print(john.generateReport())
    
    rach = Student('Rachel Kennedy')
    g.addMember(rach)
    rach.addSkill('Being Sexy')
    rach.addSkill('Math')
    rach.addSkill("Reading Comprehension")
    rach.addPoints(100, 'Being Sexy')
    rach.addPoints(50, 'Math')
    rach.addPoints(25, 'Reading Comprehension')
    print(rach.generateReport())
    
    print(g.generateReport())
    
    print(Student.students)
    

main()
