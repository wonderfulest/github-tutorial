import matplotlib.pyplot as plt
from wordcloud import WordCloud

keywords = {
    'Code hosting': 80,
    'Version control': 90,
    'Collaboration': 70,
    'Open source': 75,
    'Community': 80,
    'Git': 85,
    'Repositories': 90,
    'Pull requests': 65,
    'Issues': 70,
    'Forking': 60,
    'Branching': 65,
    'Commits': 70,
    'Continuous integration': 75,
    'Documentation': 70,
    'Social coding': 60,
    'Developers': 90,
    'Projects': 80,
    'Web-based platform': 70,
    'Workflow': 75,
    'Contributions': 80,
    'Collaborative development': 75,
    'Versioning': 85,
    'Code review': 70,
    'Bug tracking': 80,
    'Pulling changes': 65,
    'Merge conflicts': 60,
    'Issue tracking': 75,
    'Collaborative coding': 70,
    'Public repositories': 80,
    'Branch management': 65,
    'Continuous deployment': 70,
    'Documentation hosting': 60,
    'Project management': 75,
    'Collaborative workflow': 70,
    'Developer community': 90,
    'Issue management': 75,
    'Collaboration tools': 70,
    'Repository management': 80,
    'Version control system': 75,
    'Contributor community': 70,
    'Code sharing': 80,
    'Code collaboration': 75,
    'Code contribution': 70,
    'Code organization': 80,
    'Code discovery': 75,
    'Code visibility': 70,
    'Code search': 80,
    'Code analysis': 75,
    'Code quality': 70
}

# 生成词云
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(keywords)

# 绘制词云图像
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
