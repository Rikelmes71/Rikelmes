from dataclasses import dataclass


@dataclass
class SpreadsheetMatch:
    row_number: int
    car_prefix: str
    raw_row: dict


class SpreadsheetService:
    """Suporta Google Sheets API ou Excel Graph API."""

    async def find_driver_by_plan_or_observation(
        self, *, plan: str | None, guest_name: str | None
    ) -> SpreadsheetMatch | None:
        # TODO: carregar linhas da planilha corporativa
        # colunas: data | prefixo do carro | ... | plano | ... | observação
        # 1) match exato por plano
        # 2) fallback guest_name contido em observação
        return None
