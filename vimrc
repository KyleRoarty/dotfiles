set tabstop=4 softtabstop=4 shiftwidth=4
set expandtab
set shiftround
set smarttab
set titlestring="spaces"

function TabToggle()
	if &expandtab
		set titlestring="tabs"
		set noexpandtab
	else
		set titlestring="spaces"
		set expandtab
		set shiftround
		set smarttab
	endif
endfunction
nmap <F2> mz:execute TabToggle()<CR>'z

set hlsearch
"=====[ Whitespace ]================
match ErrorMsg '\s\+$'

" Remove trailing whitespace with \rtw (press and hold \ then rtw)
nnoremap <Leader>rtw :%s/\s\+$//e<CR>

"=====[ Set up line numbers and useful stuff]================
set number
set relativenumber
set showmatch
hi LineNr ctermfg=59
hi CursorLineNr ctermfg=grey

"======[ Sets tabs, spaces, line endings to show. Sets to dark grey]========
set listchars=tab:>-,trail:-,eol:$
set list
hi NonText ctermfg=59
hi SpecialKey ctermfg=59
set ffs=unix

syntax on
set title

"======[ Highlight column 80 ]==========
set cc=80
hi ColorColumn ctermbg=235
