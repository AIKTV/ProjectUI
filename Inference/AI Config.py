import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QCheckBox

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("菜单界面")
        self.setGeometry(0, 0, 1000, 1000)

        self.label = QLabel(self)
        self.label.setText("必填项")
        self.label.setGeometry(75, 50, 50, 30)

        self.model_name_input = QLineEdit(self)
        self.model_name_input.setGeometry(50, 100, 100, 30)
        self.model_name_input.setPlaceholderText("请输入使用的模型步数")

        self.wav_name_input = QLineEdit(self)
        self.wav_name_input.setGeometry(50, 150, 100, 30)
        self.wav_name_input.setPlaceholderText("请输入参考的wav干声文件名")

        self.key_num_input = QLineEdit(self)
        self.key_num_input.setGeometry(50, 200, 100, 30)
        self.key_num_input.setPlaceholderText("请输入音高")

        self.label = QLabel(self)
        self.label.setText("请选择使用的F0预测器：")
        self.label.setGeometry(50, 250, 150, 30)

        self.f0_predictor_combo = QComboBox(self)
        self.f0_predictor_combo.setGeometry(50, 300, 100, 30)
        self.f0_predictor_combo.addItem("crepe")
        self.f0_predictor_combo.addItem("pm")
        self.f0_predictor_combo.addItem("dio")
        self.f0_predictor_combo.addItem("harvest")
        self.f0_predictor_combo.addItem("rmvpe")
        self.f0_predictor_combo.addItem("fcpe")

        self.label = QLabel(self)
        self.label.setText("功能模块选择")
        self.label.setGeometry(430, 50, 100, 30)

        self.diffusion_checkbox = QCheckBox("是否使用浅层扩散模型？", self)
        self.diffusion_checkbox.setGeometry(400, 100, 200, 30)

        self.feature_retrieval_checkbox = QCheckBox("是否使用特征检索？", self)
        self.feature_retrieval_checkbox.setGeometry(400, 150, 200, 30)

        self.cluster_checkbox = QCheckBox("是否使用聚类模型？", self)
        self.cluster_checkbox.setGeometry(400, 200, 200, 30)

        self.cluster_ratio_label = QLabel(self)
        self.cluster_ratio_label.setText("请输入特征检索/聚类方案占比，范围 0-1（例：0为不使用）")
        self.cluster_ratio_label.setGeometry(310, 350, 350, 30)

        self.cluster_ratio_input = QLineEdit(self)
        self.cluster_ratio_input.setGeometry(420, 400, 100, 30)

        self.enhance_checkbox = QCheckBox("是否使用NSF_HIFIGAN增强器？", self)
        self.enhance_checkbox.setGeometry(400, 250, 200, 30)

        self.auto_predict_f0_checkbox = QCheckBox("是否使用自动音高预测？", self)
        self.auto_predict_f0_checkbox.setGeometry(400, 300, 200, 30)

        self.label_clip = QLabel(self)
        self.label_clip.setText("是否使用音频强制切片？单位为秒（例：0为自动切片，10为强制10秒切一段）")
        self.label_clip.setGeometry(270,450,600,30)

        self.input_clip = QLineEdit(self)
        self.input_clip.setGeometry(420,500,100,30)

        self.label_linear_gradient = QLabel(self)
        self.label_linear_gradient.setText("请输入两段音频切片的交叉淡入长度，单位为秒")
        self.label_linear_gradient.setGeometry(350,550,300,30)

        self.input_linear_gradient = QLineEdit(self)
        self.input_linear_gradient.setGeometry(420,600,100,30)

        self.label_cluster = QLabel(self)
        self.label_cluster.setText("是否启用聚类模型？")
        self.label_cluster.setGeometry(750, 50, 200, 30)

        self.input_cluster = QLineEdit(self)
        self.input_cluster.setGeometry(750, 100, 200, 30)

        self.label_enhance = QLabel(self)
        self.label_enhance.setText("是否启用NSF_HIFIGAN增强器？")
        self.label_enhance.setGeometry(750, 150, 200, 30)

        self.input_enhance = QLineEdit(self)
        self.input_enhance.setGeometry(750, 200, 200, 30)

        self.label_auto_predict_f0 = QLabel(self)
        self.label_auto_predict_f0.setText("是否启用自动音高预测？")
        self.label_auto_predict_f0.setGeometry(750, 250, 200, 30)

        self.input_auto_predict_f0 = QLineEdit(self)
        self.input_auto_predict_f0.setGeometry(750, 300, 200, 30)

        self.button_run = QPushButton(self)
        self.button_run.setText("运行")
        self.button_run.setGeometry(450, 770, 50, 30)
        self.button_run.clicked.connect(self.run_inference)

        self.button_diffusion = QPushButton(self)
        self.button_diffusion.setText("启用扩散")
        self.button_diffusion.setGeometry(325, 700, 100, 30)
        self.button_diffusion.clicked.connect(self.toggle_diffusion)

        self.button_enhance = QPushButton(self)
        self.button_enhance.setText("启用增强")
        self.button_enhance.setGeometry(525, 700, 100, 30)
        self.button_enhance.clicked.connect(self.toggle_enhance)

    def run_inference(self):
        model_name = self.model_name_input.text()
        wav_name = self.wav_name_input.text()
        key_num = int(self.key_num_input.text())
        f0_predictor = self.f0_predictor_combo.currentText()
        if_diffusion = self.diffusion_checkbox.isChecked()

        if if_diffusion:
            diffusion_name = input("请输入使用的扩散模型步数（例：模型为model_2000.pt就输入2000）\n：")
            diffusion_k_step = input("请输入扩散步数，越大越接近扩散模型的结果，默认100（例：100）\n：")
            print("检测到已选择启用浅层扩散，NSF_HIFIGAN增强器将被自动禁用\n")

        if_feature_retrieval = self.feature_retrieval_checkbox.isChecked()
        if_cluster = self.cluster_checkbox.isChecked()
        cluster_ratio = self.cluster_ratio_input.text()

        if if_feature_retrieval:
            print("检测到已选择启用特征检索，聚类模型将被自动禁用\n")
        elif if_cluster:
            print("检测到已选择启用聚类模型，特征检索将被自动禁用\n")

        if_enhance = self.enhance_checkbox.isChecked()
        if_auto_predict_f0 = self.auto_predict_f0_checkbox.isChecked()

        if_cluster = self.input_cluster.text()
        if_enhance = self.input_enhance.text()
        if_auto_predict_f0 = self.input_auto_predict_f0.text()

        inference_case = '.\env\python.exe inference_main.py'
        inference_case += f' -m "logs/44k/G_{model_name}.pth" -c "configs/config.json" -n "{wav_name}" -t {key_num} -s "barbara" -f0p {f0_predictor}'

        if self.button_diffusion.isChecked():
            inference_case += f' -shd -dm "logs/44k/diffusion/model_{diffusion_name}.pt" -ks {diffusion_k_step}'
        if self.button_enhance.isChecked():
            inference_case += f' -eh'
        if self.button_cluster.isChecked():
            inference_case += f' -cm "logs/44k/kmeans_10000.pt" -cr {cluster_ratio}'
        if self.button_feature_retrieval.isChecked():
            inference_case += f' --feature_retrieval -cr {cluster_ratio}'
        if self.button_auto_predict_f0.isChecked():
            inference_case += f' -a'

        if_clip = self.input_clip.text()
        if_linear_gradient = self.input_linear_gradient.text()

        inference_case += f' -cl {if_clip} -lg {if_linear_gradient}'

        subprocess.run(f'{inference_case}', shell=True)

    def toggle_diffusion(self):
        if self.button_diffusion.isChecked():
            self.button_diffusion.setText("扩散已启用")
        else:
            self.button_diffusion.setText("启用扩散")

    def toggle_enhance(self):
        if self.button_enhance.isChecked():
            self.button_enhance.setText("增强已启用")
        else:
            self.button_enhance.setText("启用增强")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    menu_window = MenuWindow()
    menu_window.show()
    sys.exit(app.exec_())
