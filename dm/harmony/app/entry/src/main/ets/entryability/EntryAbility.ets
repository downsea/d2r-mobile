// 应用入口：手机横屏全屏、电脑（自由窗口）沉浸全屏并锁内容比例，游戏前台常亮；窗口状态转成原生生命周期事件（0 失焦 1 后台 2 前台 3 激活，同安卓）。
// App entry: landscape full screen on phones, immersive full screen with a locked content aspect on PCs (free windows), screen kept on while
// the game is in front; window states become native lifecycle events (0 unfocused, 1 background, 2 foreground, 3 active, as on Android).
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { display, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';
import dm from 'libdm.so';
import { refreshForms } from '../entryformability/EntryFormAbility';

export default class EntryAbility extends UIAbility {
  // 退到后台时刷新桌面卡片（存档此时已写完）| Refresh the home-screen cards when going to the background (the saves are written by then)
  onBackground(): void { refreshForms(this.context.filesDir); }
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    AppStorage.setOrCreate('filesDir', this.context.filesDir);
    AppStorage.setOrCreate('lang', this.context.config.language ?? 'zh');
  }
  // 自由窗口：沉浸全屏启动（无标题栏、无 dock）；退出全屏后是可拖大小的窗口，内容区锁成屏幕比例，
  // 游戏按屏幕定的出图比例与触控区域在窗口里始终对得上（front_ohos.c front_game_res）
  // Free window: launch immersive full screen (no title bar, no dock); after leaving full screen the window can be resized, with the content
  // area locked to the screen aspect, so the output aspect the game picks from the screen and the touch area always match the window (front_ohos.c front_game_res)
  private static setupFreeWindow(win: window.Window): void {
    AppStorage.setOrCreate('safeLeftPx', 0);
    AppStorage.setOrCreate('safeRightPx', 0);
    AppStorage.setOrCreate('safeBottomPx', 0);
    try {
      const d = display.getDefaultDisplaySync();
      const ratio = Math.max(d.width, d.height) / Math.max(1, Math.min(d.width, d.height));
      win.setContentAspectRatio(ratio, false, false)
        .catch((e: Error) => hilog.warn(0, 'dm', 'setContentAspectRatio: %{public}s', e.message));
      hilog.info(0, 'dm', 'free window: display %{public}dx%{public}d ratio %{public}s', d.width, d.height, ratio.toFixed(3));
    } catch (e) {
      hilog.warn(0, 'dm', 'free window display: %{public}s', (e as Error).message);
    }
    win.maximize(window.MaximizePresentation.ENTER_IMMERSIVE)
      .catch((e: Error) => hilog.warn(0, 'dm', 'maximize: %{public}s', e.message));
  }
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.getMainWindow().then((win: window.Window) => {
      win.setWindowKeepScreenOn(true);
      // 自由窗口（2in1 电脑默认如此）不走手机那套：系统栏、方向、刘海在自由窗口里不生效 | Free windows (the default on 2in1 PCs) skip the phone recipe: system bars, orientation and cutout do not apply there
      let free = false;
      try { free = win.isInFreeWindowMode(); } catch (e) { hilog.warn(0, 'dm', 'isInFreeWindowMode: %{public}s', (e as Error).message); }
      if (free) {
        EntryAbility.setupFreeWindow(win);
      } else {
        win.setWindowLayoutFullScreen(true);
        win.setWindowSystemBarEnable([]);
        win.setPreferredOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
        const avoid = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_CUTOUT);
        AppStorage.setOrCreate('safeLeftPx', avoid.leftRect.width);
        AppStorage.setOrCreate('safeRightPx', avoid.rightRect.width);
        AppStorage.setOrCreate('safeBottomPx', avoid.bottomRect.height);
      }
      // 窗口模式与大小变化写进日志（全屏 / 最大化 / 浮动 / 最小化），真机核对窗口行为用 | Window mode and size changes go to the log (full screen / maximized / floating / minimized), for checking window behaviour on the device
      win.on('windowStatusDidChange', (s: window.WindowStatusType) => {
        const r = win.getWindowProperties().drawableRect;
        hilog.info(0, 'dm', 'window status %{public}d drawable %{public}dx%{public}d', s, r.width, r.height);
      });
    }).catch((e: Error) => hilog.warn(0, 'dm', 'window setup: %{public}s', e.message));
    windowStage.on('windowStageEvent', (ev: window.WindowStageEventType) => {
      const map = new Map<window.WindowStageEventType, number>([
        [window.WindowStageEventType.SHOWN, 2], [window.WindowStageEventType.ACTIVE, 3],
        [window.WindowStageEventType.INACTIVE, 0], [window.WindowStageEventType.HIDDEN, 1]]);
      const v = map.get(ev);
      if (v !== undefined) { dm.focus(v); }
    });
    windowStage.loadContent('pages/Index');
  }
}
