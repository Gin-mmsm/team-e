from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import joblib
from sklearn.metrics import classification_report, accuracy_score
# import pickle
# �f�[�^�擾
iris = load_iris()
x, y = iris.data, iris.target
# �P���f�[�^�ƃe�X�g�f�[�^�ɕ���
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state=0)
# ���f���̃C���X�^���X���쐬(�j���[�����l�b�g���[�N)
model = MLPClassifier(solver="sgd", random_state=0, max_iter=3000)
# �w�K
model.fit(x_train, y_train)
pred = model.predict(x_test)
# �w�K�ς݃��f���̕ۑ�
joblib.dump(model, "nn.pkl", compress=True)
# �\�����x
print("result: ", model.score(x_test, y_test))
print(classification_report(y_test, pred))