class ResponseFormatter:
    @staticmethod
    def format(response):
        if response is None:
            return ""

        if isinstance(response, str):
            return response

        if isinstance(response, dict):
            return ResponseFormatter._format_dict(response)

        if isinstance(response, list):
            return ResponseFormatter._format_list(response)

        return str(response)

    @staticmethod
    def _format_dict(data):
        if not data:
            return ""

        lines = []

        for key, value in data.items():
            label = ResponseFormatter._format_key(key)

            if isinstance(value, (dict, list)):
                value = ResponseFormatter.format(value)

            lines.append(f"{label}: {value}")

        return "\n".join(lines)

    @staticmethod
    def _format_list(items):
        if not items:
            return "موردی پیدا نشد."

        if all(
            isinstance(item, dict)
            and "pid" in item
            and "name" in item
            for item in items
        ):
            lines = [
                "پردازش‌های در حال اجرا",
                "",
                "PID       نام پردازش",
                "────────────────────────",
            ]

            for item in items:
                lines.append(
                    f"{str(item['pid']):<10}{item['name']}"
                )

            return "\n".join(lines)

        lines = []

        for item in items:
            lines.append(
                ResponseFormatter.format(item)
            )

        return "\n".join(lines)

    @staticmethod
    def _format_key(key):
        labels = {
            "pid": "PID",
            "name": "نام",
            "returncode": "کد خروج",
            "stdout": "خروجی",
            "stderr": "خطا",
            "total": "کل",
            "used": "استفاده‌شده",
            "free": "آزاد",
        }

        return labels.get(key, str(key))
