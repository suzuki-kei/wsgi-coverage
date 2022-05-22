import coverage
import glob
import importlib
import os
import types


def measured(target: callable) -> callable:
    """
        カバレッジを計測する.

        Arguments
        ---------
        target: callable
            target を実行中のカバレッジを計測する.

        Returns
        -------
        callable
            カバレッジを計測する処理でラップした target.

        Examples
        --------
        (1) 既存の関数を引数に呼び出す:

            wrapped_target = measured(target)

        (2) 関数を定義するときにデコレータとして指定する:

            @measured
            def target(): ...
    """
    def wrapper(*args, **kwargs):
        cov = _new_coverage()
        try:
            cov.start()
            return target(*args, **kwargs)
        finally:
            cov.stop()
            cov.save()
    return wrapper


def _new_coverage() -> coverage.Coverage:
    """
        新しい coverage.Coverage オブジェクトを生成する.

        Arguments
        ---------
        coverage.Coverage
            新しい coverage.Coverage オブジェクト.
    """
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    config_file = os.path.join(root_dir, "config", "coveragerc")
    cov = coverage.Coverage(config_file=config_file)
    cov.load()
    return cov


@measured
def import_submodules(module: types.ModuleType) -> list[types.ModuleType]:
    """
        指定したモジュールのサブモジュールを全てインポートする.

        インポート処理は measured() によってカバレッジ計測の対象となる.
        インポートされないモジュールもカバレッジレポートに含めるために使用する.

        Arguments
        ---------
        module: list[types.ModuleType]
            インポートしたサブモジュールのリスト.
    """
    files = glob.glob(os.path.join(os.path.dirname(module.__file__), '[a-zA-Z0-9]*.py'))
    names = [os.path.split(os.path.splitext(file)[0])[1] for file in files]
    submodules = [importlib.import_module('.'.join([module.__name__, name])) for name in names]
    return submodules

