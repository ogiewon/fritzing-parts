class SVGUtils:
    @staticmethod
    def has_visible_attributes(element):
        stroke = SVGUtils.get_inherited_attribute(element, "stroke")
        fill = SVGUtils.get_inherited_attribute(element, "fill")
        stroke_width = SVGUtils.get_inherited_attribute(element, "stroke-width")
        style = SVGUtils.get_inherited_attribute(element, "style")
        if style:
            style_attrs = style.split(";")
            for attr in style_attrs:
                if attr:
                    key, value = attr.split(":")
                    key = key.strip()
                    value = value.strip()
                    # Check: Avoid mixing CSS styles and SVG attributes.
                    if key == "stroke":
                        if stroke:
                            raise ValueError("Stroke attribute already defined as attribute, do not override with style.")
                        stroke = value
                    elif key == "fill":
                        if fill:
                            raise ValueError("Fill attribute already defined as attribute, do not override with style.")
                        fill = value
                    elif key == "stroke-width":
                        if stroke_width:
                            raise ValueError("Stroke-width attribute already defined as attribute, do not override with style.")
                        stroke_width = value
                    else:
                        raise ValueError(f"Unknown style attribute: {key}")

        if fill and fill != "none":
            return True
        if stroke and stroke != "none" and stroke_width and stroke_width != "0":
            return True

        return False

    @staticmethod
    def get_inherited_attribute(element, attribute_name):
        while element is not None:
            if element.get(attribute_name):
                return element.get(attribute_name)
            element = element.getparent()
        return None