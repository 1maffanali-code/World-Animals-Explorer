import matplotlib.pyplot as plt
import seaborn as sns
df = sns.load_dataset("penguins").dropna()
plt.figure()
sns.histplot(data=df, x="flipper_length_mm", kde=True, hue="species")
plt.title("Distribution with KDE Fit: Flipper Length")

# 2. Scatter Plot
plt.figure()
sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("Scatter Plot: Flipper Length vs Body Mass")

# 3. Heatmap Correlation Matrix
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Heatmap: Correlation Matrix")

plt.show()