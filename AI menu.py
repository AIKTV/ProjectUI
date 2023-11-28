import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QLabel,QLineEdit,QPushButton,QInputDialog,QMessageBox
from PyQt5.QtCore import Qt,QProcess

if_enhance = 'n'


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI语音")

        layout = QVBoxLayout()

        self.model_name_label = QLabel("请输入使用的模型步数（例：模型为G_800.pth就输入800）")
        self.model_name_edit = QLineEdit()
        layout.addWidget(self.model_name_label)
        layout.addWidget(self.model_name_edit)

        self.wav_name_label = QLabel("请输入参考的wav干声文件名，该文件应放入raw文件夹下（例：文件名为test.wav就输入test）")
        self.wav_name_edit = QLineEdit()
        layout.addWidget(self.wav_name_label)
        layout.addWidget(self.wav_name_edit)

        self.key_num_label = QLabel("请输入音高（例：维持原调为0，支持正负，数字为半音）")
        self.key_num_edit = QLineEdit()
        layout.addWidget(self.key_num_label)
        layout.addWidget(self.key_num_edit)

        self.f0_predictor_label = QLabel("请选择使用的F0预测器，0为crepe，1为pm，2为dio，3为harvest")
        self.f0_predictor_edit = QLineEdit()
        layout.addWidget(self.f0_predictor_label)
        layout.addWidget(self.f0_predictor_edit)

        self.if_diffusion_label = QLabel("是否使用浅层扩散模型？使用后可解决一部分电音问题（推荐）\n请注意该模型需先单独训练好（y/n）")
        self.if_diffusion_edit = QLineEdit()
        layout.addWidget(self.if_diffusion_label)
        layout.addWidget(self.if_diffusion_edit)

        self.diffusion_name_label = QLabel("请输入使用的扩散模型步数（例：模型为model_2000.pt就输入2000）")
        self.diffusion_name_edit = QLineEdit()
        layout.addWidget(self.diffusion_name_label)
        layout.addWidget(self.diffusion_name_edit)

        self.diffusion_k_step_label = QLabel("请输入扩散步数，越大越接近扩散模型的结果，默认100（例：100）")
        self.diffusion_k_step_edit = QLineEdit()
        layout.addWidget(self.diffusion_k_step_label)
        layout.addWidget(self.diffusion_k_step_edit)

        self.if_cluster_label = QLabel("是否使用聚类模型？聚类模型可以减小音色泄漏，但会降低模型的咬字\n请注意该模型需先单独训练好（y/n）")
        self.if_cluster_edit = QLineEdit()
        layout.addWidget(self.if_cluster_label)
        layout.addWidget(self.if_cluster_edit)

        self.cluster_ratio_label = QLabel("请输入聚类方案占比，范围 0-1（例：0为不使用）")
        self.cluster_ratio_edit = QLineEdit()
        layout.addWidget(self.cluster_ratio_label)
        layout.addWidget(self.cluster_ratio_edit)

        self.if_auto_predict_f0_label = QLabel("是否使用自动音高预测？推荐语音转换开启，歌声转换开启会严重跑调（y/n）")
        self.if_auto_predict_f0_edit = QLineEdit()
        layout.addWidget(self.if_auto_predict_f0_label)
        layout.addWidget(self.if_auto_predict_f0_edit)

        self.if_clip_label = QLabel("是否使用音频强制切片？单位为秒（例：0为自动切片，10为强制10秒切一段）")
        self.if_clip_edit = QLineEdit()
        layout.addWidget(self.if_clip_label)
        layout.addWidget(self.if_clip_edit)

        self.if_linear_gradient_label = QLabel("请输入两段音频切片的交叉淡入长度，单位为秒")
        self.if_linear_gradient_edit = QLineEdit()
        layout.addWidget(self.if_linear_gradient_label)
        layout.addWidget(self.if_linear_gradient_edit)

        self.start_button = QPushButton("开始转换")
        self.start_button.clicked.connect(self.start_conversion)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_conversion(self):
        model_name = self.model_name_edit.text()
        wav_name = self.wav_name_edit.text()
        key_num = self.key_num_edit.text()
        f0_predictor = self.f0_predictor_edit.text()
        if f0_predictor == '0':
            f0_predictor = 'crepe'
        if f0_predictor == '1':
            f0_predictor = 'pm'
        if f0_predictor == '2':
            f0_predictor = 'dio'
        if f0_predictor == '3':
            f0_predictor = 'harvest'
        if_diffusion = self.if_diffusion_edit.text()
        diffusion_name = self.diffusion_name_edit.text()
        diffusion_k_step = self.diffusion_k_step_edit.text()

        if_cluster = self.if_cluster_edit.text()
        cluster_ratio = self.cluster_ratio_edit.text()

        if_auto_predict_f0 = self.if_auto_predict_f0_edit.text()

        if_clip = self.if_clip_edit.text()
        if_linear_gradient = self.if_linear_gradient_edit.text()

        inference_case = r'.\env\python.exe inference_main.py'
        inference_case = inference_case + f' -m "logs/44k/G_{model_name}.pth" -c "configs/config.json" -n "{wav_name}" -t {key_num} -s "barbara" -f0p {f0_predictor}'

        if if_diffusion == 'y':
            inference_case = inference_case + f' -shd -dm "logs/44k/diffusion/model_{diffusion_name}.pt" -ks {diffusion_k_step}'
        if if_cluster == 'y':
            inference_case = inference_case + f' -cm "logs/44k/kmeans_10000.pt" -cr {cluster_ratio}'
        if if_auto_predict_f0 == 'y':
            inference_case = inference_case + f' -a'

        inference_case = inference_case + f' -cl {if_clip} -lg {if_linear_gradient}'

        process = QProcess()
        process.start(inference_case)
        process.waitForFinished()
        process.close()
        process.deleteLater()

        QMessageBox.information(self,"转换完成","转换完成！")


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
