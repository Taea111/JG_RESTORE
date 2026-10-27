## JG저장소 — 자료 올리기 절차

사용자는 자료를 JG저장소 아티팩트 페이지(https://claude.ai/artifact/RRufrUmc7CPLmWbM58GNUQ)에 올린다.
"GitHub에 올려 줘"라고 하면 아래 순서로 처리하고, **zip 다운로드 링크와 설명서 링크**를 답한다.

1. `ArtifactData` list `items` 로 새 자료 문서를 찾는다(`files[].parts`, `enc`, `role`).
2. 각 파트를 `Artifact` read `path=<asset id>` 로 받는다(한 번에 하나씩).
   - `enc: "b64"` 는 파트마다 base64 디코드해서 순서대로 이어 붙이고, `enc: "raw"` 는 그대로 쓴다.
   - 합친 크기가 문서의 `size` 와 같은지 확인한다.
3. `자료/<제목>/` 에 파일과 `README.md`(제목, `> 한 줄 설명`, 버전, 올린 날짜, 설명)를 넣는다.
   `python3 tools/update_list.py` 로 루트 README 목록을 고치고 main 에 커밋·푸시한다.
   GitHub 파일당 100MB 제한.
4. 링크: `https://github.com/Taea111/JG_RESTORE/raw/main/<URL 인코딩한 경로>` — curl 로 200 확인.
5. 페이지 문서에 `downloadUrl`, `downloadLabel`("zip 내려받기 (GitHub, 로그인 불필요)"), `manualUrl` 을 `if_version` 을 붙여 update 한다.

이 저장소는 공개다. 자료는 태안군청 내부용이며 zip 암호가 유일한 보호 장치다.
