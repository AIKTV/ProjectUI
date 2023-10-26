import subprocess

print("==================================================免责声明========================================================")
print(" 为避免可能的法律纠纷和道德风险，使用者在使用该整合包前，请务必仔细阅读本条款，继续使用即代表理解并同意该声明，如有异议，请立即停止使用并删除本整合包。\n")
print("1. 本整合包修改自So-VITS-SVC 4.0项目(https://github.com/svc-develop-team/so-vits-svc)，该项目目前由So-VITS社区维护。\n")
print("2. 本整合包仅为交流学习所用，在使用本整合包时，必须根据知情同意原则取得数据集音声来源的授权许可，并根据授权协议条款规定使用数据集。\n")
print("3. 禁止使用该整合包对公众人物、政治人物或其他容易引起争议的人物进行模型训练。使用本整合包产出和传输的信息需符合中国法律、国际公约的规定、符合公序良俗。不将本整合包以及与之相关的服务用作非法用途以及非正当用途。\n")
print("4. 禁止将本整合包用于血腥、暴力、性相关、或侵犯他人合法权利的用途。\n")
print("5. 任何发布到公共平台的基于So-VITS制作的作品，都必须要明确指明用于变声器转换的输入源歌声、音频，例如：使用他人发布的视频/音频，通过分离的人声作为输入源进行转换的，必须要给出明确的原视频、音乐链接；若使用是自己的人声，或是使用其他歌声合成引擎合成的声音作为输入源进行转换的，也必须加以说明。\n")
print(" 因使用者违反上述条款中的任意一条或多条而造成的一切后果，均由使用者本人承担，与整合包作者、项目作者以及So-VITS社区无关，特此声明。\n")
print(" 注意你需要至少6G以上的N卡，另外，我没有也不打算弄粉丝群 by 领航员未鸟")
print("================================================================================================================")

global diffusion_name
global diffusion_k_step
global cluster_ratio

print("\n============")
print("必填项")
print("============\n")
model_name = input("请输入使用的模型步数（例：模型为G_800.pth就输入800）\n：")
wav_name = input("请输入参考的wav干声文件名，该文件应放入raw文件夹下（例：文件名为test.wav就输入test）\n：")
key_num = int(input("请输入音高（例：维持原调为0，支持正负，数字为半音）\n："))
f0_predictor = input("请选择使用的F0预测器，0为crepe，1为pm，2为dio，3为harvest，4为rmvpe，5为fcpe\n（注：crepe即为原F0池化，使用可解决部分哑音，但可能导致部分高音跑调，默认建议rmvpe）\n：")
if f0_predictor == '0':
    f0_predictor = 'crepe'
if f0_predictor == '1':
    f0_predictor = 'pm'
if f0_predictor == '2':
    f0_predictor = 'dio'
if f0_predictor == '3':
    f0_predictor = 'harvest'
if f0_predictor == '4':
    f0_predictor = 'rmvpe'
if f0_predictor == '5':
    f0_predictor = 'fcpe'

print("\n============")
print("功能模块选择")
print("============\n")

if_diffusion = input("是否使用浅层扩散模型？使用后可解决一部分电音问题（推荐）\n请注意该模型需先单独训练好（y/n）\n：")
if if_diffusion == 'y':
    diffusion_name = input("请输入使用的扩散模型步数（例：模型为model_2000.pt就输入2000）\n：")
    diffusion_k_step = input("请输入扩散步数，越大越接近扩散模型的结果，默认100（例：100）\n：")
    print("检测到已选择启用浅层扩散，NSF_HIFIGAN增强器将被自动禁用\n")

if_feature_retrieval = input("是否使用特征检索？特征检索可以减小音色泄露，并且不是非常影响咬字\n请注意该模型需先单独训练好（y/n）\n：")
if if_feature_retrieval == 'y':
    cluster_ratio = input("请输入特征检索占比，范围 0-1（例：0为不使用）\n：")
    print("检测到已选择启用特征检索，聚类模型将被自动禁用\n")

if if_feature_retrieval != 'y':
    if_cluster = input("是否使用聚类模型？聚类模型可以减小音色泄漏，但会降低模型的咬字\n请注意该模型需先单独训练好（y/n）\n：")
    if if_cluster == 'y':
        cluster_ratio = input("请输入聚类方案占比，范围 0-1（例：0为不使用）\n：")
else:
    if_cluster = 'n'

if if_diffusion != 'y':
    if_enhance = input("是否使用NSF_HIFIGAN增强器？该选项对部分训练集少的模型有一定的音质增强效果，但是对训练好的模型有反面效果（y/n）\n：")
else:
    if_enhance = 'n'

if_auto_predict_f0 = input("\n是否使用自动音高预测？推荐语音转换开启，歌声转换开启会严重跑调（y/n）\n：")

print("\n============")
print("推理切分设置")
print("============\n")
if_clip = input("是否使用音频强制切片？单位为秒（例：0为自动切片，10为强制10秒切一段）\n：")
if_linear_gradient = input("请输入两段音频切片的交叉淡入长度，如果强制切片后出现人声不连贯可调整该数值，如果连贯建议为0，单位为秒\n：")

print("\n============")
print("推理配置清单")
print("============\n")
print(f"使用的模型：G_{model_name}.pth")
print(f"参考的干声：{wav_name}.wav")
print(f"音高调整：{key_num} key")
print(f"F0预测器：{f0_predictor}\n")

if if_diffusion == 'y':
    print(f"浅扩散模型：已启用")
    print(f"使用的扩散模型：model_{diffusion_name}.pt")
    print(f"扩散步数：{diffusion_k_step}\n")
else:
    print(f"浅扩散模型：已禁用\n")

if if_feature_retrieval == 'y':
    print(f"特征检索：已启用")
    print(f"特征检索占比：{cluster_ratio}\n")
else:
    print(f"特征检索：已禁用\n")

if if_cluster == 'y':
    print(f"聚类模型：已启用")
    print(f"聚类方案占比：{cluster_ratio}\n")
else:
    print(f"聚类模型：已禁用\n")

if if_enhance == 'y':
    print(f"NSF_HIFIGAN增强器：已启用\n")
else:
    print(f"NSF_HIFIGAN增强器：已禁用\n")

if if_auto_predict_f0 == 'y':
    print(f"自动音高预测：已启用\n")
else:
    print(f"自动音高预测：已禁用\n")

if if_clip == '0':
    print(f"音频强制切片：已禁用\n")
else:
    print(f"音频强制切片：每{if_clip}秒\n")

if if_linear_gradient == '0':
    print(f"切片交叉淡入：已禁用\n")
else:
    print(f"切片交叉淡入长度：{if_linear_gradient}秒\n")
check_menu = input("按回车键继续")
print("==================================================开始推理========================================================")

inference_case = '.\env\python.exe inference_main.py'
inference_case = inference_case + f' -m "logs/44k/G_{model_name}.pth" -c "configs/config.json" -n "{wav_name}" -t {key_num} -s "barbara" -f0p {f0_predictor}'

if if_diffusion == 'y':
    inference_case = inference_case + f' -shd -dm "logs/44k/diffusion/model_{diffusion_name}.pt" -ks {diffusion_k_step}'
if if_enhance == 'y':
    inference_case = inference_case + f' -eh'
if if_cluster == 'y':
    inference_case = inference_case + f' -cm "logs/44k/kmeans_10000.pt" -cr {cluster_ratio}'
if if_feature_retrieval == 'y':
    inference_case = inference_case + f' --feature_retrieval -cr {cluster_ratio}'
if if_auto_predict_f0 == 'y':
    inference_case = inference_case + f' -a'

inference_case = inference_case + f' -cl {if_clip} -lg {if_linear_gradient}'

subprocess.run(f'{inference_case}', shell=True)
