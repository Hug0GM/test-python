from operaciones import Calculadora


def test_class_monley(monkeypatch):
    monkeypatch.setattr(Calculadora, "sumar", lambda x: 4)
    cal = Calculadora()
    assert cal.sumar() == 4
