# 各部分控件id及对应功能
## AI配置及文件目录选择
| id                    | 类型      | 功能     | 备注  |
|-----------------------|---------|--------|-----|
| configWidget          | QWidget | 配置区域外框 ||

| id                   | 类型          | 功能         | 备注  |
|----------------------|-------------|------------|-----|
| chooseRecordGroupBox | QGroupBox   | 原始音频选择部件外框 ||
| chooseRecord         | QPushButton | 原始文件选择按钮   ||
| recordAddress        | QLineEdit   | 原始文件地址显示   ||

| id                    | 类型          | 功能          | 备注  |
|-----------------------|-------------|-------------|-----|
| chooseHandledGroupBox | QGroupBox   | 处理后音频选择部件外框 |     |
| chooseHandled         | QPushButton | 处理后文件选择按钮   |     |
| handledAddress        | QLineEdit   | 处理后文件地址显示   ||

| id           | 类型          | 功能       | 备注         |
|--------------|-------------|----------|------------|
| configButton | QPushButton | AI模型配置菜单 | 由 fAx1A 负责 |

## 录音控制模块
| id                  | 类型          | 功能         | 备注             |
|---------------------|-------------|------------|----------------|
| recordWidget        | QWidget     | 录音区域外框     ||
| recordTimeDisplay   | QLabel      | 录音时长显示     | 更新时需要加上前面中文    |
| recordButtonWidget  | QWidget     | 录音启停按钮外框   ||
| recordButton        | QPushButton | 录音开始结束按钮   | 默认开始，录音时为结束    |
| pauseRecordButton   | QPushButton | 录音暂停继续按钮   | 默认暂停，暂停时为继续    |
| recordOutputDisplay | QLabel      | 录音文件保存路径显示 | 默认空白，录音保存时显示路径 |

## 播放模块
| id         | 类型      | 功能     | 备注  |
|------------|---------|--------|-----|
| playWidget | QWidget | 播放区域外框 ||

| id               | 类型          | 功能         | 备注          |
|------------------|-------------|------------|-------------|
| recordPlayBox    | QGroupBox   | 原始音频播放区域   ||
| recordPlayButton | QPushButton | 原始音频播放按钮   | 默认开始，播放时为暂停 |
| recordStopButton | QPushButton | 原始音频播放停止按钮 | 始终为结束       |

| id                | 类型          | 功能          | 备注          |
|-------------------|-------------|-------------|-------------|
| handledPlayBox    | QGroupBox   | 处理后音频播放区域   ||
| handledPlayButton | QPushButton | 处理后音频播放按钮   | 默认开始，播放时为暂停 |
| handledStopButton | QPushButton | 处理后音频播放停止按钮 | 始终为结束       |

| id         | 类型     | 功能      | 备注               |
|------------|--------|---------|------------------|
|playFrame| QFrame | 滑动进度条外框 | 内部内容由 xiubi44 负责 |