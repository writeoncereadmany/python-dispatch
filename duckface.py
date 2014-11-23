class Duckface:
  def __init__(self, *required_attributes):
    self.required_attributes = required_attributes

  def satisfied_by(self, instance):
    return all((hasattr(instance, attrib) for attrib in self.required_attribs))